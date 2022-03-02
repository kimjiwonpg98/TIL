# type과 interface의 차이점

예제

```ts
interface People {
  name: string
  age: number
}

const peoples: People = {
  name: "지원",
  age: 26,
}

type PeopleType = {
  name: string
  age: number
}

const peopless: PeopleType = {
  name: "지수",
  age: 30,
}
```

> 보다시피 사용하는 방법은 다르지 않다...

- 예제 interface
```ts
interface People {
  name: string
}

interface People {
  age: number
}

const people: People = {
  name: "John",
  age: 30
}
// 오류 x 자동으로 확장이 된다.
```


- 예제 type
```ts
type People = {
  name: string
}

type People = {
  age: number
}

const people: People = {
  name: "John",
  age: 30
}
// Error: Duplicate identifier 'People'
```

> 예제를 보면 type은 새로운 속성을 추가하기 위해서 다시 같은 이름으로 선언할 수 없지만 interface는 항상 선언적 확장이 가능하다. <br> 그리고 interface는 객체에만 사용이 가능하지만 type은 문자열도 가능하다.