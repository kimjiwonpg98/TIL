## 1. 이 주제를 다루는 이유

pk를 **auto_increment**로 지정 후 insert로 값을 추가하는 API를 만들고 있었다.
그리고 확인하는데 insert 실패한 경우를 넘어 3에서 10으로 바로 pk값이 넘어가 있었다.🙄
그래서 한 번 알아보았다.


## 2. insert 실패 시에도 증가하는 이유

> 이유부터 간단하게 말하면 auto_increment_lock_mode 때문이다.


#### auto_increment_lock_mode 값의 차이 (0 ~ 2)

##### 1.  0일 때 (tranditional)
모든 insert를 대상으로 테이블 레벨의 AUTO_LOCK를 사용한다.
**insert 결과를 예측하여 인덱스의 순서를 보장하기 위해 모든 구문마다 락을 걸어 검사한다.**
그래서 auto_increment로 되어 있는 인덱스의 순서를 보장하기 위해선 이 설정을 해주면 된다.


##### 2. 1일 때 (consecutive)
기본값으로 지정되어 있는 설정이다.
구문마다 락이 걸리지만 할당 프로세스 단위로 락이 걸린다.
AUTO_INCREMENT values의 할당 과정에서만 mutex를 이용해서 동시 접근을 제어하기 때문에 확장성을 높일 수 있다.

##### 3. 2일 때 (interleaved)
락을 사용하지 않는다.
확장성은 가장 높지만 복구가 어렵다는 단점이 있다. 왜냐하면 복구/복제용 로그를 사용하지 않는 경우에만 사용이 가능하기 때문이다.
단순히 유니크 값은 지켜주지만 실행 순서에 따라 단조적으로 올라가기 때문에 순차적이지 못한 auto_increment값이 나타날 수 있다.


> 결론적으로 0일 때는 인덱스의 순서를 보장하지만 모든 구문마다 락을 걸어 검사하기 때문에 성능이 가장 떨어지고 2는 순차적이지 않게 저장될 가능성이 크다. 그래서 필자는 insert 실패 시를 그냥 넘어가고 성능을 위해 1로 사용하기로 했다!


## 3. auto_increment_lock_mode를 바꾸는 방법


```sql
SET GLOBAL auto_increment_lock_mode = 0
```

이 방법을 사용했을 때

> Variable 'innodb_autoinc_lock_mode' is a read only variable

이 에러가 뜬다면

우분투는 /etc/mysql/mysql.conf.d/mysql.cnf 에서
window는 C:\ProgramData\MySQL\MySQL Server 8.0\my.ini 에서

**innodb_autoinc_lock_mode = 0** 을 적으면 된다.


## 참고 블로그

- https://stuffdrawers.tistory.com/11
- https://kkensu.tistory.com/16
