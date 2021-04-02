# target

addEventListener같은 메서드같은 콜백메서드에서는 파라미터를 주지 않으면 default값으로 event가 파라미터로 간다.

그래서 받는 함수에서 event.target을 하면 클릭한 값이 나온다.

ex)

```js
const table = document.querySelector("table");

table.addEventListener("click", result);

function result(e) {
  const button = e.target;
}
```

table안에 있는 element를 누를 경우 그 값이 나오게 된다.

2021.03.04
