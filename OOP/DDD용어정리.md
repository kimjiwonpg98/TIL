## DDD 용어정리

도메인 주도 설계라는 뜻으로 도메인을 중심으로 설계하는 방법론이다.
이 글에서는 내가 DDD를 이해하고자 할 때 필요한 용어들을 정리하고자 한다.


### BOUNDED CONTEXT

```md
시스템을 논리적으로 나누는 경계를 의미
각 BOUNDED CONTEXT는 특정 도메인 모델을 포함하며, 다른 BOUNDED CONTEXT와 명확히 구분된다.
```

- 하나의 BOUNDED CONTEXT는 하나의 팀이 관리해야 한다.
  - 여러 팀이 관리하게 되면 충돌을 야기할 수 있다.
- 하나의 팀은 여러 개의 BOUNDED CONTEXT를 관리할 수 있다.
- 각각의 BOUNDED CONTEXT는 각각의 개발 환경을 가질 수 있다.

각 도메인을 운영할 때 필요한 규칙들

### 유비쿼터스 언어

- 도메인에서 사용할 용어들을 사전에 기록하고 명확하게 정의함으로써 다른 사람들도 공통된 언어로 소통할 수 있도록 함
  - ex) 병원 플랫폼에서의 user는 환자가 된다.


### VALUE OBJECT (VO)

- 불변 객체
  - 객체의 상태를 변경할 수 없다.
  - 상태가 변경되지 않음으로 여러 스레드가 동시에 접근해도 충돌이나 일관성 문제가 발생하지 않는다.
- 객체의 식별성이 아닌 객체의 속성을 기반으로 동등성을 판단한다. 
- 의미를 명확하게 표현해야한다. 두 개 이상의 데이터가 개념적으로 하나인 경우 벨류 타압을 사용한다.

### ENTITY

- 식별자를 가지고 있는 객체
  - 객체의 상태가 변경될 수 있다.
  - 객체의 식별자가 같다면 동일한 객체로 판단한다.

### AGGREGATE

- 관련된 객체들을 하나로 묶은 것
- 루트 엔티티가 존재한다.
  - 루트 엔티티는 AGGREGATE의 진입점이며 외부에서 AGGREGATE에 접근할 때는 반드시 루트 엔티티를 통해 접근해야 한다.
  - 내부 객체들은 외부에서 직접 접근할 수 없고 루트 엔티티를 통해서만 접근할 수 있다. **(캡슐화)**
- 내부의 객체들은 일관성을 유지해야 한다 -> 경계를 넘어서는 트랜잭션은 최소화해야 한다.
- 작고 응집력 있게 설계해야 한다. 너무 큰 AGGREGATE는 관리가 어렵고 성능 문제를 야기할 수 있다.
  - 클수록 트랜잭션이나 락이 걸리는 범위가 넓어지기 때문에 성능 문제가 발생할 수 있다.

- 참조 시 주의할 점
```md
두 개의 트랜잭션이 내포되지 않도록 주의해야 한다.
ID를 이용한 참조 방식을 사용하면 복잡도를 낮추는 것과 함께 한 애그리거트에서 다른 애그리거트를 수정하는 문제를 원천적으로 방지할 수 있다
```

### 리포지토리(Repository)

- 애그리게잇을 저장하고 조회하는 인터페이스
- 데이터베이스와 도메인 모델 간의 추상화 계층 제공

### 도메인 서비스(Domain Service)

- 특정 애그리게잇에 속하지 않는 도메인 로직을 캡슐화
- ex) 할인 정책, 배송 비용 계산

### Aggregate Root (애그리게잇 루트)

- aggregate의 진입점
- aggregate 내 객체들의 일관성을 유지하는 책임을 가짐