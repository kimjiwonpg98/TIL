# cloudfront 설정

- 이 글은 s3에 있는 이미지를 불러오기 위한 작업으로 이루어져 있다.

### s3 설정

기본적으로 외부에서 s3에 접근할 수 없도록 퍼블릭 엑세스 차단을 설정해준다.
![s3퍼블릭](https://user-images.githubusercontent.com/75289370/226086473-49b65c38-6daa-4ff4-9e0b-cfcd56e1991f.png)

특정 외부 계정에서만 접근 가능하도록 엑세스 제어 목록에서 추가해준다. (cloudfront와 코드상의 계정)
![acl](https://user-images.githubusercontent.com/75289370/226086509-84cea344-1e91-4699-a3b9-b9be9806793e.png)


### IAM 설정
```
  코드에서 사용할 사용자와 lamdba@edge에서 사용할 역할
```

- 첫번째로 코드 상에서 사용할 IAM 사용자를 생성한다. 
    - arn:aws:iam::aws:policy/service-role/AmazonS3ObjectLambdaExecutionRolePolicy
    - arn:aws:iam::aws:policy/AmazonS3FullAccess
- 처음 만들 때 암호를 잘 저장해두어야 한다.
![admin](https://user-images.githubusercontent.com/75289370/226087147-a45532f2-2fc5-4f87-80fe-40f566d15395.png)


- 두번째로 lambda@edge에서 사용할 역할을 만들어준다.
  - s3에서 객체를 받아오고 cloudfront를 업데이트하는 권한들이 들어있다.
  - cloudfront에 이벤트가 들어올 때마다 log를 남기기 위해 log 관련 권한도 있다.
  
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "iam:CreateServiceLinkedRole",
                "lambda:GetFunction",
                "lambda:EnableReplication",
                "cloudfront:UpdateDistribution",
                "s3:GetObject",
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents",
                "logs:DescribeLogStreams"
            ],
            "Resource": "*"
        }
    ]
}
```

### lambda에서 사용할 코드 추가

- 압축을 위해 sharp를 사용하는데 리눅스 기반이기 때문에 리눅스 버전으로 설치해줘야한다.
```
npm install --platform=linux --arch=x64 sharp
```

```js
'use strict';

const querystring = require('querystring'); // 설치 x
const AWS = require('aws-sdk'); // 설치 x
const Sharp = require('sharp');

const S3 = new AWS.S3({
    region: 'ap-northeast-2'
});
const BUCKET = 'moaeblog';

const allowedExtension = [
    "jpg",
    "jpeg",
    "png",
    "webp",
    "heic",
    "JPG",
    "JPEG",
    "PNG",
];

exports.handler = async (event, context, callback) => {
    const { request, response } = event.Records[0].cf;
    // Parameters are w, h, f, q and indicate width, height, format and quality.
    const params = querystring.parse(request.querystring);

    // Required width or height value.
    if (!params.w && !params.h) {
        return callback(null, response);
    }

    // Extract name and format.
    const { uri } = request;
    const [, imageName, extension] = uri.match(/\/?(.*)\.(.*)/);

    // Init variables
    let width;
    let height;
    let format;
    let quality;
    let resizedImage;
    let s3Object;

    // Init sizes.
    width = parseInt(params.w, 10) ? parseInt(params.w, 10) : null;
    height = parseInt(params.h, 10) ? parseInt(params.h, 10) : null;

    // Init quality.
    if (parseInt(params.q, 10)) {
        quality = parseInt(params.q, 10);
    }

    // Init format.
    format = params.f ? params.f : extension;
    format = format === 'jpg' ? 'jpeg' : format;
    format = format === "HEIC" ? "jpeg" : format;

    // 이미지 파일이 아니라면 500 error
    if (!allowedExtension.includes(extension)) {
        response.status = "500";
        response.headers["content-type"] = [
            { key: "Content-Type", value: "text/plain" },
        ];
        response.body = `${extension} is not allowed`;
        callback(null, response);
        return;
    }

    // For AWS CloudWatch.
    console.log(`parmas: ${JSON.stringify(params)}`);
    console.log(`name: ${imageName}.${extension}`);

    try {
        s3Object = await S3.getObject({
            Bucket: BUCKET,
            Key: decodeURI(imageName + '.' + extension)
        }).promise();
    } catch (error) {
        console.log('S3.getObject: ', error);
        return callback(error);
    }

    try {
        resizedImage = await Sharp(s3Object.Body)
            .resize(width, height, { fit: "inside" })
            .toFormat(format, {
                quality
            })
            .toBuffer();
    } catch (error) {
        console.log('Sharp: ', error);
        return callback(error);
    }

    const resizedImageByteLength = Buffer.byteLength(resizedImage, 'base64');

    if (resizedImageByteLength >= 1 * 1024 * 1024) {
        response.status = "404";
        response.headers["content-type"] = [
            { key: "Content-Type", value: "text/plain" },
        ];
        response.body = `${request.uri} is not found. ${error}`;
        return callback(null, response);
    }

    response.status = 200;
    response.body = resizedImage.toString('base64');
    response.bodyEncoding = 'base64';
    response.headers['content-type'] = [
        {
            key: 'Content-Type',
            value: `image/${format}`
        }
    ];
    return callback(null, response);
};
```

코드 자체는 많이 돌아다니기 때문에 따로 설명은 안하도록 하겠다.


### cloudfront 설정

![Cloudfront](https://user-images.githubusercontent.com/75289370/226087626-e784665a-2e26-47c4-8e0f-b60cdafb2303.png)

- 서울 지역만 사용하기 때문에 지역을 설정해주고 도메인도 기본적으로 주는 도메인으로 할 것이기 떄문에 그것으로 설정해준다.


![cloudfrontsetting](https://user-images.githubusercontent.com/75289370/226087692-3220d1af-4c17-472d-89ce-28ebb4adf7df.png)

- 캐시 및 원본 요청은 위의 lambda 코드가 옛날 코드이기 때문에 legacy cache settings로 해주었다.ㅎㅎ

가장 아래 함수 연결은 lambda 에서 lambda@edge 배포를 하게 되면 알아서 설정이 된다.

최신화가 되었지만 lambda 설정은 아직 부족해보인다ㅠ


그래도 이렇게 설정하게 되면 사용자는 cloudfront로만 이미지에 접근할 수 있고 s3 접근은 코드 상으로만 가능하기 때문에 만족스럽다!