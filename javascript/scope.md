# 📚 Scope

## 스코프란?

간단하게 말해서 함수나 변수의 유효범위를 스코프라고 한다.

하지만 자바스크립트는 다른 언어와 다른 특징이 있음으로 주의해야한다.

> 모든 식별자(변수이름, 함수이름, 클래스 이름)는 자신이 선언된 위치에 의해 다른 코드가 식별자 자신을 참조할 수 있는 유효 범위(scope)가 결정된다.

## 종류

코드에서는 전역과 지역으로 나눌 수 있다.

|구분|설명|스코프|변수
|--|--|--|--|
|전역|코드의 가장 바깥 영역|전역 스코프|전역 변수
|지역|함수 몸체 내부|지역 스코프|지역 변수

- 지역 변수는 자신의 지역 스코프와 하위 지역 스코프에서만 유효하다.


## 렉시컬 스코프

EX)
```js
let x = 1;
function foo() {
  let x = 10;
  bar();
}

function bar() {
  console.log(x);
}
bar();  // ?
foo();  // ?
```

이 예제의 실행 결과는 bar함수의 상위 스코프가 무엇인지에 따라 결정된다.

여기서 두가지 패턴을 예측할 수 있는데

1. **함수를 어디서 호출** 했는지
2. **함수를 어디서 정의** 했는지

첫 번째 방식이라면 foo함수에서 정의한 x변수의 값인 10이 나와야하고 두번째 방식이라면 전역변수로 정의한 x변수의 1값이 나와야한다.

> 첫 번째 방식을 **동적 스코프**라고 한다.
<br> 호출되는 시점에서 상위 스코프를 결정하기 떄문이다.

> 두 번쨰 방식은 **렉시컬 스코프(정적 스코프)**라고 한다.
<br> 상위 스코프가 동적으로 변하지 않고 함수가 정의되는 부분에서 상위 스코프가 정해진다.


두 번째 방식인 정적 스코프가 대부분의 프로그래밍 언어에서 따르는 방식이다. 물론 자바스크립트도 이 방식을 따른다.

그래서 위 예시의 답은 두 개 모두 1이다.

bar함수를 정의한 부분이 전역이기 때문에 전역 변수인 x의 값을 참조하게 된다.


## ⚠ 전역변수의 사용을 최대한 줄이는 것이 좋다.


### 🤔 이유

1. 검색 속도가 느리다.

- 전역 변수는 **스코프 체인 상 종점**에 존재한다.
- 그러므로 가장 마지막에 검색되기 때문에 검색 속도가 가장 느리다.

2. 생명주기가 길다.

- 전역변수는 실행이 종료될 때까지 계속 유지되기 때문에 메모리 리소스를 오랜 시간 소비한다.


### 🔮 해결방법 몇가지

1. 즉시 실행 함수

함수형 프로그래밍에서 많이 사용하는데 즉시 실행 함수를 사용하면 지역변수를 사용하고 바로 메모리 리소스에서 삭제되기 때문에 전역 변수를 생성하지않고 사용할 수 있다.

2. 네임스페이스 객체

- 전역으로 네임스페이스 역할을 담당할 객체를 생성하고 그 안에 변수를 추가하는 방법이다.

ex)

```js
const jo = {
  name: "Lee",
  address: "seoul"
}
```

- 이 방법은 딱히 좋아보이진 않는다.

3. 모듈 패턴

class를 이용해 private constructor를 이용해서 할 수 있다.

끝!





