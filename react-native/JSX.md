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