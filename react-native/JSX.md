# 📖 JSX

자바스크립트의 확장 문법

JSX
```js
function formatName(user) {
  return user.firstName + ' ' + user.lastName;
}

const user = {
  firstName: "jiwon",
  lastName: "Kim",
};

const element = <h1>Hello, {formatName(user)}!</h1>;
```
기존JS
```js
const element = React.createElement(
  `h1`,
  null,
  `Hello`,
  formatName(user),
  '!'
);
```

휠신 간단하다!

## 🐱‍🏍JSX는 여러 개의 요소를 표현할 경우 하나의 부모로 감싸야 한다.

ex)
```js
export default function App() {
  return (
    <View style = {styles.container}>
      <Text>HIHI</Text>
      <StatusBar style="auto"/>
    </View>
  );
}
```
✨View는 html의 div와 비슷한 역할하는 컴포넌트

## 🐱‍🏍 JSX에서 AND와 OR
1. and연산자를 사용하면 앞의 조건이 참일 경우 뒤의 내용이 나타난다.
2. or연산자를 사용하면 앞의 조건이 거짓인 경우 내용이 나타난다.

ex)
```js
{name === "jiwon" && <Text>My name is {name}</Text>}
```

## 🐱‍🏍 JSX에서 null과 undefined
null은 허용<br>undefined 오류