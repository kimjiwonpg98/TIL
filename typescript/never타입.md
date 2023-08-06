## Never 타입

- never의 의미
- 왜 사용해야 하는가?
- never 사용법


세가지에 대해 간단하게 적어보도록 하겠다.

### 1. never의 의미

일단 never는 타입의 한 종류이다.

여기서 타입은 가능한 값의 집합이다. ts를 사용하다보면 type 지정을 해줄 때가 은근 많다.

```ts
const age: number = 13;
const name: string = "jiwon";

const country: string = 12; // type error
```
해당 변수에 타입을 지정하게 되면 해당 변수는 오직 가능한 집합 내의 값만 가질 수 있게 된다.

never는 **집합 내에 어떤 값도 없는 것**을 나타낸다.

`모든 값을 나타내는 any도 never에 속할 수는 없다.`

```ts
declare const any: any;
const never: never = any // error
```

### 2. 왜 사용해야 할까?

타입 시스템 중에는 그 어떤 것도 `불가능`하다는 타입이 필요하다.
 
필자가 아는 타입 중에는 `undefined`나 `null` 같이 없다를 나타내는 타입들이 있다. 

```md
물론 `undefined` 은 변수를 선언하고 값을 할당하지 않은 상태이고 
`null` 은 변수를 선언하고 빈 값을 할당한 상태(빈 객체)이다ㅎㅎ
```

`void`라는 타입도 있지만 `void`는 함수가 함수 요청자에게 아무것도 리턴하지 않는다를 나타내는 타입이다.

위 타입으로는 불가능을 표현할 수 없기 떄문에 `never` 타입을 사용한다.

그리고 이 불가능이라는 뜻은 ts 에서는 다음과 같이 의미한다고 한다.

- 어떤 값도 가질 수 없는 빈 타입 
  - 제네릭 및 함수에서 허용되지 않는 파라미터 
  - 호환 되지 않는 타입 교차 
  - 빈 유니언 타입 (유니언 했지만 아무것도 안되는 경우)

그럼 결론적으로 위 의미를 나타내기 위해 never 타입을 쓰게 될 것이다.


### 3. never 사용법

위에서 never를 왜 사용하는지 알게 되었다.

하나하나 찾아보면 될 것 같다.

- **함수에 올 수 있는 파라미터에 제한을 거는 용도**

```ts
type Read = {}
type Write = {}
declare const toWrite: Write

declare class MyCache<T, R> {
  put(val: T): boolean
  get(): R
}

declare class ReadOnlyCache<R> extends MyCache<never, R> {}

const readonlyCache = new ReadOnlyCache<Read>()
readonlyCache.put(toWrite); // error
readonlyCache.get();
```

위 예시는 getter로 사용하기 위한 타입 지정이다.
T 부분에 never 타입을 지정함으로써 요청 파라미터를 제한하여 getter 역할만 수행하도록 하는 것이다.

- **조건문에서 철저한 일치를 보장하기 위한 용도**

```ts
function notFoundError(data: never) {
    throw new Error('not found error');
}

type Color = 'red' | 'green' | 'blue'

function getColorName(c: Color): string {
    switch (c) {
        case 'red':
            return 'is red'
        case 'green':
            return 'is green'
        default:
            return notFoundError(c) // 그 외의 string으로 불가능
    }
}
```

- **부분적으로 구조적 타이핑을 허용하지 않기 위한 용도**

```ts
type VariantA = {
    a: string,
}

type VariantB = {
    b: number,
}

declare function fn(arg: VariantA | VariantB): void

const input = {a: 'foo', b: 123 }
fn(input) 
```
ts에서는 위 예제가 허용이 된다.

```ts
type VariantA = {
    a: string
    b?: never
}

type VariantB = {
    b: number
    a?: never
}

declare function fn(arg: VariantA | VariantB): void

const input = {a: 'foo', b: 123 }
fn(input) // 속성 'a'의 타입은 호환되지 않는다.
```
never를 사용해 구조적 타이핑을 비활성화 시킬 수 있다.

- **무한 루프나 node 강제 종료 방지**

```ts
function throwError(): never {
    throw new Error();
}

let foo: string | undefined;

if (!foo) {
    throwError();
}

foo; // string

// or

const checkFoo = foo ?? throwError(); // string
```

never 타입으로 함수 실행이 끝난 후 호출자에게 제어권을 주지 않고 바로 반환한다.


### 반대로 never가 되는 경우

- 타입이 호환되지 않는 경우 (여러 타입이 교차되는 경우)

`string`와 `number`는 타입이 호환되지 않는 경우의 대표적인 예시이다.

```ts
function f1(obj: { a: number, b: string }, key: 'a' | 'b') {
    obj[key] = 1;    // 'number' 타입은 'never'타입에 할당할 수 없다.
    obj[key] = 'x';  // 'string' 타입은 'never'타입에 할당할 수 없다.
}
```
ts에서 사용하면 위 처럼 에러가 나는 것을 볼 수 있다.
 
이유는 string과 number타입 모두가 호환되어야한다는 제약 조건이 추가되었기 떄문이다.

우리가 교차되는 경우에 사용하려면 타입 단언 (as) 을 하거나 함수 오버로드를 고려해봐야 할 것이다.

참고한 페이지에 더 잘 정리되어있지만 생각 정리 겸 정리해보았다.

never 를 좀 더 잘 활용한다면 타입답게 사용할 수 있을 것 같다는 생각이 든다. - 끝 -


### 참고

- [Toast](https://ui.toast.com/posts/ko_20220323)
- [블로그](https://yceffort.kr/2022/03/understanding-typescript-never)



