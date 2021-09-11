# Hoisting

> 함수 밖에서 선언한 전역 범위의 변수를 최상단에 선언하고     
> 함수 안에 선언한 함수 범위 변수는 해당 함수의 최상위로 선언된다.

## 대상

1. var

var로 함수나 변수 선언 시 호이스팅이 발생

ex

```js
console.log(name);
// jiwon이 할당 되어 값 표시
var name = "jiwon";
```

2. 함수 선언식

함수 선언식 역시 호이스팅이 발생

```js
catName("Chloe");

function catName(name) {
  console.log("My cat's name is " + name);
}
```


