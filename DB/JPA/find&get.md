## find와 get의 차이

### find

- 실제 객체 즉시 로딩
- 호출했을 때 DB로 SELECT 쿼리 호출
- 값이 존재하지 않을 때 null 응답
- 기본적으로 Optional로 되어있음

#### 사용목적
- 데이터 조회해서 바로 사용할 때


### get

- 객체 호출 시 가짜 객체 반환 (지연 로딩)
- 이미 알고 있는 데이터를 조회할 때는 SELECT X (getId())
- 그 외의 컬럼을 조회할 때 SELECT해서 객체 값을 채움
- 값이 존재하지 않을 때는 EntityNotFoundException 예외 발생

#### 사용목적
- 연관관계의 데이터가 필요할 때 (실제 데이터가 아닌 ID 객체가 필요할 때)
- product의 fk인 user_id가 필요할 때 user 넣기 위해 사용
- @Transactional 밖에서 이 객체를 조회하면 없는 객체이기 때문에 예외가 발생함을 주의해야함
