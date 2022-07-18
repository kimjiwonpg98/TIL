## 힘든 에러 핸들링

각 router마다 하나하나 try-catch로 감싸준다.

```javascript
app.get("/user", async function (req, res, next){
  try {
    const users = await db.collection("User").find().toArray();
  } catch (error) {
    res.status(500).json({ error: error.toString() });
  }
  res.json({ users });
});

```
모든 코드에 try-catch문을 적용하는 것은 상당히 귀찮고 비효율적인 일이다.
만약 여러 에러 상황이 있다면 하나하나 모두 바꿔줘야한다.

## Error Handling Middleware 정의

그래서 기본적으로 express에서는 errorMiddleware를 사용한다.
`err, req, res, next` 이렇게 4개의 인자를 가지고 있는 미들웨어는 에러 핸들링 미들웨어이다.
```js
import express from 'express';
const app = express();

app.get('*', function(req, res, next) {
  throw new Error('error');
});

app.use(function(error, req, res, next) {
  // Any request to this server will get here, and will send an HTTP
  // response with the error message 'woops'
  res.json({ message: error.message });
});

app.listen(3000);
```
첫 번째 라우터가 에러를 던지면, 마지막에 작성한 에러 핸들링 미들웨어까지 내려가서 오류를 처리한다. 에러 핸들링 미들웨어는 반드시 마지막에 작성해야 한다.

보여주기 위해 app.use에 그대로 작성했지만 사용할 때는 따로 파일을 만들어서 사용한다.


기존 비동기 오류


1. 콜백안에서 처리 or next
```js
import express from 'express';
import fs from 'fs';

const app = express();

app.get('*', async function(req, res, next) {
  // fs.readFile함수는 error면 콜백함수에 전달
  fs.readFile('/file.txt', (err, data) => { // 에러 발생
    if (error) {
      res.sendStatus(404).send('file not found');
      // next(error); // 혹은 미들웨어의 마지막 안전망에 던지기
    }
  });  
});

app.use(function(error, req, res, next) {
  // Will get here
  res.json({ message: error.message });
});

21app.listen(3000);
```

2. promise (errorhandler는 똑같으니 생략)
```js
app.get('*', async function(req, res, next) {
  // fsAsync는 promise
  fsAsync.readFile('/file.txt')
  	.then((data) => {...})
    .catch(error => {
      res.sendStatus(404).send('error');
    })
    //.catch(next); 혹은 미들웨어의 마지막 안전망에 던지기  
});
```
promise에는 then catch 문이 있어서 그쪽에서 해결하거나 next로 보내준다.

## 비동기 시(async) 오류

async 사용 시 발생하는 오류는 다음과 같이 next()를 통해 에러 핸들링 미들웨어로 넘겨야 한다.

그냥 throw 해버리면 결과값이 promise이기 때문에 에러 핸들링 미들웨어까지 도달하지 못한다.
결국 try catch문으로 엮어서 next()로 보내게 되는데 찾아보니 데코레이터 패턴을 사용하여 wrapper 함수를 만들어 사용하는 방법도 존재했다.

- wrapper 사용
```js
// wrapper 사용 (데코레이터 패턴)
const wrap = asyncFn => {
  return (async (req, res, next) => {
    try {
      return await asyncFn(req, res, next)
    } catch (error) {
      return next(error)
    }
  })  
}

router.get('/', wrap(async (req, res, next) => {
  const result = await foo();
  res.send(result);
}))
```
```js
function wrapAsync(fn) {
  return function(req, res, next) {
    fn(req, res, next).catch(next);
  };
}
```
wrapAsync로 감싼 모습이다. 비동기 에러가 발생하면 catch->next를 거쳐 사전에 정의한 에러 핸들링 미들웨어로 에러가 넘어간다. 이 때 error의 종류에 따라 다른 메세지를 건네주는 등 간결한 코드 작성이 가능해진다.

다른 방법으로는 모듈을 사용하는 방법이 있다.

case 1.
express-asyncify

case 2.
async-middleware