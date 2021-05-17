# CORS(Cross-Origin Resource Sharing)

그냥 간단하게 해석해보면 **교차 출처 리소스 공유**이다

>추가 HTTP 헤더를 사용해서 한 출처에서 실행 중인 웹 Application이 
>다른 출처의 선택한 자원에 접근할 수 있는 권한을 부여하도록 브라우저에 알려주는 체제


- XMLHttpRequest (GET, POST, PATCH, PUT, HEAD) 등을 사용할 때 동작한다!
- CORS 설정을 하지 않으면 다른 도메인에서 요청을 받지 못하게 된다.



## 🔗 종류
--------------------------------
<br>

## 1. Simple requests
--------------------------------
<br>

1) 충족해야하는 조건

|메서드|Content-Type|
|--|--|
|GET|application/x-www-form-urlencoded|
|POST|multipart/form-data|
|HEAD|text/plain|




2) 실행 순서

브라우저가 서버로 전송 => 요청 헤더의 Origin을 보고 어디서 요청왔는지 확인

🔮 **Access-Control-Allow-Origin**: 접근 가능한 도메인을 적음 (*은 모든 도메인 허용)

<br>

## 2. preflighted  requests
--------------------------------
<br>

옵션 메서드를 통해 전송이 안전한지 먼저 1차 확인 (preflighted: 미리 전송)

![CORS](https://user-images.githubusercontent.com/75289370/118500138-83274900-b762-11eb-96ee-323c4be17a70.png)
**redirect를 지원하지 않는다!**

 *Access-Control-Allow-Headers* 의 값을 "X-PINGOTHER, Content-Type" 으로 전송하여 실제 요청에 헤더를 사용할 수 있음을 확인

<br>

## 3. Request with credentials
--------------------------------

<br>

인증 정보를 포함한 요청으로 credentials 속성을 추가해서 요청을 보낸다.

![CORS2](https://user-images.githubusercontent.com/75289370/118501212-735c3480-b763-11eb-82df-7a29aa66bd0d.png)

> 예를 보면 GET 메서드이기 때문에 preflighted하지 않아도 credentials이 true가 아니라면 응답을 거부한다.

**fetch 시 credentials 속성**

|값|설명|
|--|--|
|same-origin|같은 출저 간 요청에만 인증 정보를 담는다
|
|include|모든 요청에 인증 정보를 담는다
|
|Omit|모든 요청에 인증 정보를 담지 않는다
|