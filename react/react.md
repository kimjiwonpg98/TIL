# REACT에 관한 공부

## react에서 동작하는 방식

<br/>

App.js에서

```js
function App() {
  return <div>Hello</div>;
}
```

<br/>

이 부분을 index.js에서 rendering
src -> index.js에서 `document.getElementById("root")`를 사용

<br/>

그러면 public -> index.html에서 div의 아이디가 root인 곳에 출력할 값을 보내준다. 2/10

### 👿 window에서 wsl로 실행시 실시간 변경이 되지 않을때 이슈

<br>
내부 디렉터리에서 **.env** 파일만들어서 **CHOKIDAR_USEPOLLING=true** 입력
<br>
입력하게 되면 리눅스 루트 파일 시스템 이외의 마운트된 디렉터리를 찾아서 자동으로 갱신해준다.<br>
이유: 가상환경에서 발생하는 오류 중 하나

CLICK LINK [참고자료](https://create-react-app.dev/docs/troubleshooting/#npm-start-doesnt-detect-changes)

## JSX(JavaScriptXml)

리액트에서만 실행되는 문법으로
중괄호{}를 이용해 안에 함수를 넣거나 자바스크립트의 문법을 사용할 수 있고<br> html의 문법도 사용할 수 있다! 2/10

- 그래서 **재사용**도 가능하게 된다!!
- key와 value로 사용가능
