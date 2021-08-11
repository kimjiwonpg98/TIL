# IMAGE 처리방법

## 1. Image 컨테이너 생성

1. Content Delivery에서 Image 컨테이너를 만듭니다.
2. 자신이 저장할 폴더를 만듭니다.
3. 만들게 되면 URL과 Appkey, SecretKey가 생성됩니다.

## 2. 백엔드에서 API 사용법

🔮 API를 사용하기 위해서 필요한 공통 정보가 있습니다.
- 보안 키 인증 처리입니다.
- 헤더 측에 **Authorization** 보안 키를 넣어서 요청해야합니다.

⭐postman에서 사용하는 방법
- Authorization란에 들어가 type에서 OAuth 2.0을 선택합니다.
- Access Token란에 SecretKey를 입력 후 Header Prefix부분을 빈 부분으로 만들어줍니다.

- AWS와 다르게 API 작동이 NHN 측에서 되는 것이기 때문에 백엔드에서 따로 코드를 짤 필요가 없습니다.

## 3. 프런트에서 API 사용방법

- header에 secretKey를 넣어줍니다.
```js
headers = {
  Authorization: "secretKey",
}
```
- axios의 경우 url을 자신이 사용할 url을 적어줍니다.
- header부분도 url과 params같이 axios에 넣어줍니다.


- [사용자 API 가이드](https://docs.toast.com/ko/Contents%20Delivery/Image/ko/api-guide/)


### 3. 느낀점

>백엔드에서 API를 만들지 않아도 된다는 점은 확실히 편한 것 같지만
>header같은 부분에서 조금 더 설명이 필요할 것 같습니다.