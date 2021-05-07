# 📃 This란?

## 💫 현재의 가리키는 값을 의미하는데 이것은 함수 실행 방식마다 달라진다!

<br>

```
중요!

1. 함수 실행시에는 전역(window) 객체를 가리킨다.

2. 메소드 실행시에는 메소드를 소유하고 있는 객체를 가리킨다.

3. 생성자 실행시에는 새롭게 만들어진 객체를 가리킨다.

4. arrow Function은 Lexical this => 자신이 둘러싼 this 계승
```

## 1. 전역 문맥
--------------------------
**웹 브라우저 한정**

```
this는 window 전체를 참조한다.

그래서 전역 객체 모두를 참조할 수 있다.

window 항상 true
```

**Node 한정**
```
global 항상 true
```

<br>

## 2. 일반 함수 function() {} 
--------------------------------

1. 엄격모드가 아닐 때 

    ```js
    const test = {
      prop: 42,
      func: function () {
        return this.prop;
      },
    };

    console.log(test.func());
    // expected output: 42
    ```
    객체 안에 있을 때 그 객체의 값을 이용한다.

    사람들이 설명할 때 전역 객체를 참고한다고 하는데
    해본 결과 전역 객체를 받아오지 못한다.(?)

    브라우저인 경우에만 `window` 객체에 바인딩 된다라고 알고 있으면 될 것 같다.

2. 엄격모드일 때 **("use strict" 입력했을 때)**

    `undefined`로 초기화된다!


## 2. 애로우 함수 () => {} 
--------------------------------

자신을 감싼 스코프에서만 사용된다.

전역 코드인 경우에는 전역 객체를 가리킨다.

```js
function objFunction() {
  console.log("Inside `objFunction`:", this.foo); // 13
  return {
    foo: 25,
    bar: () => console.log("Inside `bar`:", this.foo), // 13
  };
}

objFunction.call({ foo: 13 }).bar();
```
이렇게 가까운 곳에서 입력된 값을 계승받아 이용한다.

그래서 사용하면 안되는 경우가 있다

<br>

## 2-1. 에로우 함수를 사용하면 안되는 경우
--------------------------

### 1. 메서드
  - 기존 함수
     ```js
    const test = {
      prop: 42,
      func: function () {
        return this.prop;
      },
    };

    console.log(test.func());
    // expected output: 42
    ```
  - arrow 함수
    ```js
    const test = {
      prop: 42,
      func: () => {
        return this.prop;
      },
    };

    console.log(test.func());
    // expected output: undefined
    ```
  자신의 상위 환경의 this가 없기 때문에 undefined가 뜨게 된다.

### 2. Prototype
  - 메서드와 마찬가지로 상위 환경 this가 없어 undefined가 뜨게 된다.

### 3. 생성자
  - arrow함수는 익명함수이기 때문에 prototype 속성이 없다.
  ```js
  const Test = () => {
    console.log(this);
  }

  const test = new Test();
  //TypeError: Test is not a constructor
  ```

## 3. 생성자
--------------------------

new 키워드를 이용해서 함수를 호출하게 되면
{} 로 빈 객체가 반환하게 된다.

그 다음 prototype과 this로 만들어진 변수들의 값이 빈 객체에 들어가게 된다.

**여기서 this는 생성자의 기본 반환값 역할을 하게 된다.**

```js
function Test() {
  this.name = () => {
    console.log("this is test");
  };
}

const test = new Test();

test.name(); //"this is test"
```
<br>

## 4. call, apply, bind 메서드
--------------------------
```js
function test() {
  console.log(this.name);
}

var obj = { name: 'test' };
test.call(obj); // test
test.apply(obj); // test
(test.bind(obj))(); // test
```

  ### 1. call 메서드
    함수명.call(this값, 매개변수 무제한)
  ### 2. apply 메서드
    함수명.apply(this값, [매개변수로 전달되는 배열])
    🔮 2개의 인자만을 전달해야한다! 무조건 배열!
  ### 3. bind 메서드
    함수명.bind(this값, 매개변수1, 매개변수2, ...)
    🔮 원본 함수를 새로운 함수로 복제



<br>






##### 참고자료
https://kim-solshar.tistory.com/57