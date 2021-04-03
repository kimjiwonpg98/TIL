# fs 모듈

fs 모듈은 파일 시스템에 접근하는 모듈

파일을 생성하거나 삭제, 읽거나 쓰기 가능

사용 방법

```js
const fs = require("fs");

fs.readFile("./readme.txt", (err, data) => {
  if (err) throw err;
  console.log(data); //버퍼 데이터로 나온다.
  console.log(data.toString()); // txt파일의 내용
});
```

fs는
<span style="color: #F15F5F">**콜백 형식 모듈**</span>

```js
const fs = require("fs").promises;

fs.readFile("./readme.txt")
  .then((data) => {
    console.log(data.toString());
  })
  .catch((err) => console.error(err));
```

그래서 이렇게 <span style="color: #F15F5F">**프로미스 형식**</span>으로 바꿔주는 방법을 사용

백준같은 경우는 readLine을 사용해서 데이터를 입력받을 때 사용하기도 한다!!

파일 쓰기 같은 경우는 writeFile

fs.access(경로, 옵션, 콜백) : 폴더 or 파일에 접근할 수 있는지 체크

fs.mkdir(경로, 콜백) : 폴더를 만드는 메서드
등등

<br>
2021/02/25
