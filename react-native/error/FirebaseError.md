# Firebase 관련 에러

1. FirebaseError: Firebase: Firebase App named '[DEFAULT]' already exists (app/duplicate-app)
--------------------------------
firebase가 실행되고 있는데 또 지정되어서 나는 에러이다.

```js
//기존
const app = firebase.initializeApp(config);
//config는 {}(json 형식으로 key같은걸로 들어갑니다.)

//해결
if (!firebase.apps.length) firebase.initializeApp(config);
const app = firebase.app();
```
firebase.app()는 실행되고 있는 firebase를 가리킨다.
