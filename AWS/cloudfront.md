# 👨‍💻 cloudFront로 이미지 캐시 서버 구축

[aws cloudFront 바로가기](https://console.aws.amazon.com/cloudfront/home?region=us-east-1#)
**cloudFront는 region할 필요 없다.**

![cloudFront](https://user-images.githubusercontent.com/75289370/119069534-42108c80-ba21-11eb-8127-fe390d2cea20.PNG)
- Origin Domain Name: 생성한 버킷 이름으로 선택
- Restrict Bucket Access: 버킷의 접근 제한을 활성화
- Origin Access Identity: S3의 접근 권한을 얻기 위한 새로운 Identity 생성 (알아서 생성됨)
- Grant Read Permissions on Bucket: 선택한 S3 의 버킷 정책에 읽기 권한을 자동으로 생성.
![cloudFront1](https://user-images.githubusercontent.com/75289370/119072240-1fcd3d80-ba26-11eb-8bfa-8632669ad8ca.PNG)
Cache and origin request settings에서 Use legacy cache settings를 클릭 <br>
💫 여기서 저는 여기서 cors 정책에 의해 403에러로 이미지를 불러오지 못하는 경우가 생겨 기본 s3 cors 정책을 사용했습니다.

![cloudFront2](https://user-images.githubusercontent.com/75289370/119072253-2491f180-ba26-11eb-9f85-8090004eea05.PNG)
params를 이용해 이미지 압축을 진행할 예정이므로
- Query String Forwarding and Caching에서 all 선택
- Query String Whitelist에  d=1024x1024 이런식으로 구현할 예정이므로 d를 써준다.
- Compress Objects Automatically: 리소스 자동 압축 기능 허락


![cloudFront3](https://user-images.githubusercontent.com/75289370/119072257-265bb500-ba26-11eb-9222-dce7f0e48635.PNG)
- 아시아에서 사용하므로 all이 아닌 Asia가 포함되는 선에서 선택


### behaviors 
설정에서 Behaviors로 들어간 후 자신이 원하는 폴더를 path pattern에 board/* 이런식으로 설정

패턴의 우선순위를 줄 수 있다!

### 이렇게 마치게 되면 cloudfront에서 제공하는 임시 도메인으로 이미지를 불러올 수 있다.


## 참고 자료
> [cloudFront 세팅](https://devhaks.github.io/2019/08/25/aws-lambda-image-resizing/) 