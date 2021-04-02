# child_process

노드에서 다른 프로그램을 실행하고 싶거나 명령어를 수행하고 싶을 때 사용하는 모듈

현재 노드 프로세스 외에 새로운 프로세스를 띄워서 명령을 수행하고
노드 프로세스에 결과를 알려줌

그래서 child_process

### 3가지의 종류 스트림

1. child.stdin: 표준 입력
2. child.stdout: 표준 출력
3. child.stderr: 표준 에러

## exec를 사용했을 때

```js
const exec = require("child_process").exec;

const process = exec("dir");

process.stdout.on("data", (data) => {
  console.log(data.toString()); //실행결과
});

process.stderr.on("data", (data) => {
  console.error(data.toString());
  //실행 > 에러
});
```

## spawn을 사용했을 때

```js
const spawn = require("child_process").spawn;
const process = spawn("ls", [-a]);
//or
const python = spawn("python", ["test.py"]);

python.stdout.on("data", (data) => {
  console.log(data.toString()); //실행결과
});

python.stderr.on("data", (data) => {
  console.error(data.toString());
  //실행 > 에러
});
```

## exec와 spawn의 차이

exec : 셸을 실행해서 명령어를 수행한다.
<br>
spawn : 새로운 프로세스를 띄우면서 명령어를 실행

2021/02/25
