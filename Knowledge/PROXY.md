# PROXY SERVER

## 개념

1. 클라이언트와 서버 사이에서 데이터 요청과 응답을 대신 받아주는 역할
2. 보안상의 문제로 직접 통신을 주고 받을 수 없는 사이에서 프록시 서버가 중계하는 역할을 합니다.

![proxy](https://user-images.githubusercontent.com/75289370/120199236-fbf7cc00-c25d-11eb-88e9-4b40f01b6724.PNG)

## 종류

### 1. Forward PROXY
![image](https://user-images.githubusercontent.com/75289370/120199293-09ad5180-c25e-11eb-811c-fb37b7dd4b5b.png)

1. 클라이언트가 인터넷에 직접 접근 X  => 프록시 서버가 서버에 접근   
2. 프록시 서버가 요청을 받아 인터넷에 연결   
**클라이언트의 정보를 감출 수 있습니다.**   
3. Cache를 사용해 자주 사용하는 정적 데이터는 서버에 들릴 필요 없이 프록시 서버에서 충당합니다.   
=> 여기서 오는 장점:    
저장된 내용을 보내주게 되면 전송 시간을 
절약할 수 있고 외부 트래픽도 줄어드는 장점으로 
네트워크의 병목 현상도 방지할 수 있습니다.



### 2. Reverse PROXY

![image](https://user-images.githubusercontent.com/75289370/120199448-35303c00-c25e-11eb-819c-626295391522.png)


클라이언트가 인터넷에 데이터를 직접 요청   
내부 서버가 아니라 리버스 프록시 서버에 요청   
클라이언트가 요청하는 마지막 포인트는 프록시 서버 도메인이기 때문에 서버의 정보를 감출 수 있습니다.   
내부 서버의 설정을 이용해 **로드 밸런싱**과 **서버 확장**에 유리합니다.   
