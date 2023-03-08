## Row Level Locking

- 행 수준의 잠금으로 같은 테이블의 행들에 대한 액세스는 허용될 수 있는 잠금이다.


### SELECT FOR UPDATE

```markdown
데이터를 수정하기 위해 SELECT 하는 중이기 떄문에 다른 트랜잭션이 레코드를 SELECT하지 못하게 read, write 락을 건다.
```

- 명령어
  - SELECT * FROM 테이블 WHERE 조건 FOR UPDATE;

- 다른 트랜잭션은 락이 걸려있는 레코드는 조회 & 수정이 불가능하다.
- FOR UPDATE를 사용한 트랜잭션이 커밋이 되어야 락이 풀린다.
- 기본적으로는 락을 획득할 때까지 무한정 기다린다.
  - NOWAIT 같은 옵션을 주어 락을 기다리지 않도록 할 수도 있다.


### SELECT FOR SHARE

```markdown
특정 레코드에 write 락 & shared 락을 건다.
```

- 명령어
  - SELECT * FROM 테이블 WHERE 조건 LOCK IN SHARE MODE;

- SELECT의 대상 레코드를 write 락을 걸어 수정을 불가능하게 한다.
  - SELECT FOR UPDATE 와 다르게 조회는 가능하다.
- LOCK IN SHARE MODE를 사용한 트랜잭션이 커밋되어야 락이 풀린다.
- 여러 트랜잭션이 read lock을 얻을 수 있으며 수정하려는 트랜잭션은 락이 풀리기를 기다려야한다.



[참조글](https://dev.mysql.com/doc/refman/5.7/en/innodb-locking-reads.html)