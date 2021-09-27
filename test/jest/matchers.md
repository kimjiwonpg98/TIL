## 1. 개요

Jest는 보통 함수의 반환값을 인자로 받는 **expect** 함수를 제공한다.
그리고 그 인자를 토대로 결과값을 **expectation** 객체로 반환해준다. 

이 과정에서 비교하려는 값과 실제 값을 비교하는 메소드가 필요하게 된다. 그것들을 Matchers라고 부른다.

## 2. matchers


### 표로 정리한 matchers


|함수명|설명|
|--|--|
|.toEqual|객체의 내용이 같은지 확인|
|.toStrictEqual|엄격한 toEqual로 undefined 허용 X|
|.toBeNull|오직 Null과 같은지 확인|
|.toBeUndefined|오직 undefined와 같은지 확인|
|.toBeDefined|undefined가 아닌지 확인|
|.toBeTruthy|true값인지 확인|
|.toBeFalsy|False값인지 확인|
|.toMatch|정규 표현식을 이용해 문자열이 포함되어 있는지 확인|
|.toContain|배열이나 반복하는 객체가 특정 요소를 포함하는지 확인|
|.toThrow|함수가 호출될 때 에러를 던지는지 확인|
|.toBeCalled|실행한 함수에 기대한 함수가 호출되는지 확인|
|.toBeCalledWith|기대한 함수의 결과값에 포함이 되는지 확인|


## 3. toBe를 사용하지 않는 이유

Jest의 공식 페이지를 가면 toBe 대신 toEqual을 사용하는 것을 권장한다.


**test.js**(테스트하려는 코드)
```js
const test {
	person: (firstName, lastName) => ({firstName, lastName})
}

module.exports = test;
```

**jest.spec.js**(테스트)
```js
const make = require("../test.js");

const me = make.person("jiwon","kim");

describe("toBe와 toEqual 차이", () => {
  
  test("toBe", () => {
      expect(me).toBe({"jiwon","kim"});
  });
  //실패
  
  test("toEqual", () => {
      expect(me).toEqual({"jiwon","kim"});
  });
  //성공
}
```


> 사실 toBe와 toEqual 둘 다 원시적인 타입(string, number, boolean, null)에서는 같은 역할을 한다.
하지만 객체에서는 달라진다.


**toBe**는 그 객체가 어느 메모리에 위치하는지도 따져서 확인한다. 그래서 위의 예시에서도 결과가 실패가 뜨게 된다.

**toEqual**은 그 객체의 값만 보고 비교하기 때문에 위 예시에서는 성공이 뜬다.


javascript를 예시로 비교하면 **<span style="color:orangered">==은 toBe</span>**, **<span style="color:#40f7f1">===은 toEqual</span>**로 비교할 수 있다.




---
## 참고


https://jestjs.io/docs/using-matchers

