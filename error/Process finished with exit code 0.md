## 문제 🚨

application 실행 후 `Process finished with exit code 0` 발생 후 application이 종료

에러메시지도 없어 어리둥절했다.

![](https://velog.velcdn.com/images/kimjiwonpg98/post/3f6bda1a-8f0b-4fa8-bef7-ca72a85d60d8/image.png)

에러 메시지도 뜨지 않아 혼란이였다.

## 원인

내장 톰켓에서 application을 읽지를 못하는 문제라고 한다.

문제가 될 상황은 여러 개가 있는데

1. port를 이미 다른 서비스가 선점하고 있을 때
2. `org.springframework.boot:spring-boot-starter-web` 의존성 추가

## 해결

필자는 멀티모듈로 설정하고 있어

`org.springframework.boot:spring-boot-starter-web`를 까먹었다..ㅎ

결론: 당황하지말고 설정부터 보자!

