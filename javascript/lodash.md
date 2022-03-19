## 1. 📖 개념

lodash는 javascript의 한 라이브러리다.
보통의 경우 array, collection, date 등 데이터의 필수적인 구조를 쉽게 다룰 수 있게 하는데에 사용된다. 
JavaScript에서 배열 안의 객체들의 값을 handling(배열, 객체 및 문자열 반복 / 복합적인 함수 생성) 할 때도 사용한다.
이러한 점으로 인해 JavaScript의 코드를 줄여주고, 빠른 작업에 도움이 된다.
\_.변수 이런식으로 작성할 경우 lodash wrapper로 변수를 감싸게 되고 해당 변수에 대한 chaining을 시작하게 된다.

결론적으로 기본적으로 사용하는 것보다 퍼포먼스적인 면에서 더 효율적이기 때문에 많이 사용하고 있다.


## 2. 📚 lodash의 메서드

### 1. _.findIndex()

> 형식: _.findindex(array,[predicate=.indentity],[thisArg])
입력: object의 배열
출력: index number

example
```js
const example = [
  { name: "james", age: 25 },
  { name: "jude", age: 30 },
  { name: "curry", age: 23 },
  { name: "koan", age: 21 },
];

_.findIndex(example, (people) => {
    return people.age > 26;
  });
// 1
```

> 관련 함수
**_.findLastIndex** 뒤에서 부터 일치하는 index 반환

### 2. flatten()

> 형식: _.flatten(array, [isDeep])
다차원 배열 내의 요소를 관리
depth를 명시하지 않으면 1depth까지만 풀어준다.
입력: 다차원 배열
출력: 결과 배열

```js
_.flatten([1, [2, 3, [4]]]);
//[ 1, 2, 3, [ 4 ] ]
_.flatten([1, [2, 3, [4]]], true);
// [1, 2, 3, 4]
```

여러 층으로 만들어진 array를 하나의 층 즉, 하나의 array의 정도는 중요하지 않으나 Shallow에 true값이 부여되면, single level로 통일된다.

### 3. remove()

> 형식: .remove(array, [predicate=.indentity],[thisArg])
출력: 제거된 배열
배열 내의 조건에 맞는 요소들 제거한 후에 반환

example
```js
const array=[1,2,3,4];

let evens=remove(array,function(n){
   return n % 2 === 0;
});

console.log(array);
//-> [1,3]

console.log(evens);
//-> [2,4]
```

이 메서드 말고도 다른 메서드들과 연결하여 사용할 수 있다.

관련 메서드들을 많이 참고해서 사용한다면 효율적인 코드를 짤 수 있을 것 같다.