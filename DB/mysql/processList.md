서버를 사용하는 도중에 mysql Connection이 끊기거나 SQL error가 생기는 일이 종종 있습니다.    
그럴때 상태를 확인하는 방법을 알아보겠습니다.


## 👨‍💻 상태확인

- 일단 mysql에 접속해줍니다.

> mysql -u root -p

- 현재 processlist를 확인하면 총 몇개의 쓰레드가 동작하고 있는지 확인할 수 있습니다.


> show processlist;

- 혹은 where절을 이용 할 수도 있습니다.
- 이 예시는 사용되고 있는 쓰레드를 보기 위함입니다.

> SELECT * FROM information_schema.processlist where command != 'sleep';


![process](https://images.velog.io/images/kimjiwonpg98/post/0f740c49-eab3-4496-99ac-f034eefc84c8/progress.PNG)

|Id|User|Host|db|Command|Time|State|Info|Progress|
|--|--|--|--|--|--|--|--|--|
|연결 아이디|사용자|IP|사용한DB이름|실행중인 명령 타입|현재 상태를 유지한 초|스레드 상태|실행중인 SQL|진행률|



