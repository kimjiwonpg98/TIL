저는 nginx로 로드밸런싱을 설정하는 도중에 too many connections라는 에러가 떳습니다.    
검색해보니 mysql이나 mariadb에서 종종 일어나는 에러라고 하는데 많이 만날 에러인듯하니 정리해보겠습니다.😂


## 1. 원인 찾기

### 👨‍💻 상태확인

- 일단 mysql에 접속해줍니다.

> mysql -u root -p


> show variables like "%max_connections%";

![max_connection](https://images.velog.io/images/kimjiwonpg98/post/80ad7d19-6141-4240-b6f1-3e7d1ce45254/max_connnections.png)

- max_connections: 최대 접속수
- 기본값은 **151**이다!
- 나는 이미 설정했기때문에 2000으로 되어 있다.

> show status like "%connect%";

![connect](https://images.velog.io/images/kimjiwonpg98/post/5b2096a3-6caa-414d-b366-5f7da64ffbe9/connect.png)

- **Aborted_connects**: MySQL 서버에 접속이 실패된 수
- **Connections**: 연결된 쓰레드 수
- **Max_used_connections**: 최대로 동시에 접속한 수
- **Threads_connected**: Thread Cache의 Thread 수

> show status like '%thread%';

![thread](https://images.velog.io/images/kimjiwonpg98/post/9f8aff1f-463a-47a6-9139-98b6f1ded012/thread.png)


- **Threads_connected**: 현재 연결된 Thread 수
- **Threads_created**: 접속을 위해 생성된 Thread 수
- **Threads_running**: Sleeping 되어 있지 않은 Thread 수

-----------

위의 내용을 보고 Rate를 계산할 수 있습니다.

방법은

> Cache Miss Rate(%) = Threadscreated / Connections x 100

⭐ Cache Miss Rate(%) 가 높다면 thread_cache_size를 기본값인 8 보다 높게 설정하는 것이 권장됩니다.

> Connection Miss Rate(%)= Abortedconnects / Connections x 100    

⭐ Connection Miss Rate(%) 가 1% 이상이 된다면 wait_timeout 을 좀 더 길게 가져가는 것이 좋습니다!

> Connection Usage(%) = Threads_connected / max_connections x 100

⭐ Connection Usage(%)가 100% 라면 max_connections 수를 증가시키는 것이 좋습니다.

⭐⭐⭐ connection 수가 부족할 경우 too many connections 에러가 발생합니다!!!


-------------



## 2. 해결방안


### 1. max_connections 변경

프로젝트에서 mariadb를 사용하기 때문에 경로가 mysql과는 살짝 다릅니다.

> 경로: /etc/mysql/mariadb.conf.d/50-server.cnf

50-server.cnf안에서 max_connections를 위에서 계산했을 때 나온 적당한 값으로 변경해준다.

**여기서 단순히 max_connections만 바꾼다고 완벽하게 해결되지 않습니다.**


>#### 해결되지 않는 이유 2가지
1. 최대 연결 갯수를 늘린 것이기 때문에 메모리 용량이 꽉차면 연결을 허용해도 과부하가 걸려 처리 불가능!
2. 최대 연결 갯수를 넘어가면 또 too many connections 오류 발생!

### 2. wait_timeout 변경

- wait_timeout은 **mysqld와 client가 연결을 맺은 후, 다음 쿼리까지 기다리는 최대 시간**이다. 
- ⭐ 즉 API 요청이라고 볼 수 있다!
- wait_timeout안에 요청이 들어오면 다시 0으로 초기화됩니다.
- too many connections 에러가 뜨지 않기 위해선 바꿔줘야한다. 왜냐하면 기본값이 무려 **28800초(8시간)...**

50-server.cnf안에서 저같은 경우는 3600으로 했습니다.

👷‍♂️ 하지만 트래픽이 많다면 30초같이 적게 하는 것이 좋습니다!


### 3. Connection Pool 설정 변경

![mariadb](https://images.velog.io/images/kimjiwonpg98/post/55816159-215f-419b-8d8c-c324254d7243/maria.png)

내 경우에는 백엔드와 연결 시 connectionLimit을 5로 하고 있었습니다.    
기본값은 10이지만 max_connections과 맞게 300으로 주었습니다.


### 추가 내용 interactive_timeout
- interactive_timeout은 터미널 모드 (ex: mysql>)에서의 다음 쿼리까지 기다리는 최대 시간입니다.
- 이것도 기본값이 28800초이니 3600초로 하는 것을 권장한다고 합니다!


### 4. 리부팅!

가장 중요한 작업입니다. 이 값들을 적용하기 위해서 mysql을 재부팅해줍니다.

> service mysql restart

------------



이렇게 해결방법을 다 하고 processlist를 보면 ConnectionLimit만큼의 쓰레드가 있는 것을 확인할 수 있습니다!

[processlist보는법](https://velog.io/@kimjiwonpg98/mysql-processlist%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%B4-%EC%93%B0%EB%A0%88%EB%93%9C-%EC%83%81%ED%83%9C-%ED%99%95%EC%9D%B8#-%EC%83%81%ED%83%9C%ED%99%95%EC%9D%B8)




-------


### 🙇‍♂️ 참고

- [time_out 참조](https://knight76.tistory.com/entry/30031445050)
- [튜닝 참조](https://plogger.tistory.com/entry/MySQL-Too-many-connections-Max-Connection-%EC%A1%B0%EC%A0%95)

