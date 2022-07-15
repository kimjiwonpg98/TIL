## 개념

- 각종 웹, 모바일에서 타사의 API를 사용하고 싶을 때 권한을 획득하기 위한 프로토콜이다.
- OAuth는 Open Authorization의 약자로 서비스 이용자를 대신해서 서비스를 요청할 수 있도록 자원 접근 권한을 위임하는 방법이다.

#### OAuth1.0과 OAuth2.0의 차이점

- 2.0에서 access token life time이 추가되어 보안이 강화되었다.


## 용어 정리

1. Resource Owner: 액세스 중인 리소스의 유저 (user)
2. Client: Resource owner를 대신하여 보호된 리소스에 액세스하는 응용프로그램 (oauth를 요청하는 쪽)
3. Resource server: client의 요청을 수락하고 응답할 수 있는 서버
4. Authorization server: Resource server가 액세스 토큰을 발급받는 서버
5. Authorization code: access token을 발급받기 전에 필요한 code
7. Access token: 보호된 리소스에 접근할 수 있는 권한을 받기 위한 token

## OAuth2.0 동작과정

![image](https://velog.velcdn.com/images/kimjiwonpg98/post/f52597e6-5d02-4904-bcc9-7baf780886ab/image.png)
괴랄한 글씨체지만 한 번 그림을 그려보는게 이해가 빠를 것 같아 플로우를 그려보았다.
그림으로 표현한 이 내용은 평소에 우리가 자주 사용하는 네이버 로그인이나 카카오 로그인처럼 간편 로그인에 대한 플로우다.
(그리고 난 다음 resource server가 authorization server라는 것을 알았다..ㅎㅎ)

> 1. user가 로그인 요청을 한다.
2. 클라이언트(oauth api 입장)는 로그인 페이지를 보여준다.
3. 서비스 로그인 페이지로 넘어가고 로그인을 시도한다. 그 과정에서 인증처리를 한다.
4. resource server에서 code를 받게 되면 인증처리가 완료된 것이다.
5. 할당받은 code와 기존에 가지고 있던 client_id와 client secret key로 access token과 refresh token을 받는다.
6. access token으로 resource server에서 user의 개인 정보를 조회할 수 있게 된다.

![](https://velog.velcdn.com/images/kimjiwonpg98/post/1d1c3a9e-2d16-4cf2-a0cb-5a62acecd5ea/image.png)

위에서 그린 내용과 똑같지만 깔끔한 플로우 정리라서 가져왔다.




참고

https://onepinetwopine.tistory.com/389