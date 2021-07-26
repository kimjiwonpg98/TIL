# lamdba

## AWS의 대표적인 서버리스 컴퓨팅 서비스입니다.

### ⭐ 서버리스 컴퓨팅 서비스란?

- 서버가 없다는 뜻이 아니라 **보이지 않는 곳에 관리형 서버**가 있다고 해석할 수 있습니다.
- 특정 이벤트가 발생하면 서버를 실행하는 컴퓨팅 서비스입니다.
- 서버리스 컴퓨팅 작동 원리
![serverless](https://user-images.githubusercontent.com/75289370/126998921-ec7865fb-0c01-4b98-97a4-0dc09bf21bf3.jpg)



## Lambda 함수

- AWS Lambda에서 실행하는 코드를 Lambda 함수라고 합니다.
- 코드를 AWS Lambda에 업로드한 후에 특정 AWS 리소스 ( S3, CloudFront, DynamoDB테이블 등)에 연결할 수 있습니다.
- 그럼 정해둔 특정 이벤트가 발생할 때 Lambda 함수의 코드가 실행됩니다.

## 장점!

1. 개발에만 집중할 수 있는 환경
2. 서버에 대해 고민할 필요가 없습니다. (이벤트 발생 시 실행되기 때문)
3. 비용이 저렴(트래픽이 많이 나오지 않을 시)
4. 서버 뿐 아니라 여러 리소스에서 사용이 가능

## 단점!
1. 로그 보는데 불편 (cloudwatch를 통해 볼 수 있지만 추가 요금)
2. 동시 실행에 대한 제한