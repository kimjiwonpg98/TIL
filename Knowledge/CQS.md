## 📋 Init

어떤 언어를 이용하든 함수를 이용하게 된다.

그 함수들 중에서도 같은 기능이지만 원시값의 상태를 변화시키는 함수와 원시값은 유지하면서 그 원시값을 기반으로 결과를 반환하는 함수가 있다.

이런 차이를 command와 query로 볼 수 있다.

필자와 같이 일하는 분의 기억법을 잠깐 빌려 한국어로 번역하여 뜻을 생각해보기로 했다.

command와 query를 한국어로 번역해보면 명령과 질의이다.

> 
query는 **질의**다. 
질문이 있으면 답이 있을 것이다. 답변을 해준다!
command는 **명령**이다.
명령? 그저 따르기만 하면 된다...(군대 ptsd가 오려고 한다..😨)


간단하게 정의를 적어보자

>`query`는 상태를 변화하지 않으면서 결과를 반환하는 것을 말한다. (side effect가 없다!)

>`command`는 결과는 반환하지 않으면서 상태를 변화하는 것을 말한다.

이 정의들은 둘을 나눠야한다라는 원칙으로 학자들이 만들게 되었고 그 원칙이 바로 CQS이다.

## 👨‍💻 코딩편 example


필자는 node를 주로 하고 있으니 node를 기반으로 설명해보겠다.

`query`

```js
const exampleArray = [1, 2, 3, 4];

console.log(exampleArray.slice(1));
// [2, 3, 4]

console.log(exampleArray);
// [1, 2, 3, 4]
```
slice 함수를 사용하게 되면 기존 배열을 변경하지 않으면서 새로운 배열 객체로 반환하게 된다.
이런 경우 상태는 변화하지 않으면서 결과를 반환하기 때문에 query로 볼 수 있다.


`command`

```js
const exampleArray = [1, 2, 3, 4];

exampleArray.splice(0, 1);

console.log(exampleArray);
// [2, 3, 4]
```

splice 함수는 기존 배열을 변경하면서 결과값은 반환하지않는다.

이렇게 같은 역할을 하는 함수이지만 query와 command로 나눌 수 있다!


## 🐱‍👤 예외사항

stack의 pop를 CQS의 예외사항으로 많이 뽑고 있다.

pop은 stack에서 값이 제거되고 가장 최근에 추가된 값이 반환되기 때문이다.

> CQS를 만든 마틴 파울러는 CQS 원칙을 지키는 것도 좋지만 유용한 상황이 생긴다면 얼마든지 깨뜨릴 준비가 되있다고 하였었다. - 섞어서 쓴다고 나쁜 것은 아니다!


## 👨‍💻👩‍💻 개발에서의 CQS


- 데이터를 조회하는 GET
- 데이터를 업데이트하는 PUT & PATCH
- 새로운 데이터을 추가하는 POST
- 데이터를 삭제하는 DELETE

정도가 있을 것 같다.

기본적으로 GET같은 조회가 query
값을 변환시키고 반환이 없는 나머지가 command가 될 수 있다.

하지만 코딩을 하다보면 데이터를 추가하고 그 값을 반환시켜주는 경우도 있다. (CQS원칙을 깬 경우)

그렇지만 조회는 내부의 변경이 없는 메서드로 설계하도록 노력하는 것이 좋다고 생각한다. (side effect가 날 수도 있기 떄문에)


## 마무리




> 이 CQS를 공부하면서 느낀점은 개발한 **메서드를 호출 했을 때 내부에서 변경(사이드 이펙트)가 일어나는 메서드**인지 아니면 **내부에서 변경이 일어나지 않는 메서드**인지 확실하게 분리하는 것이 가장 중요하다는 점이다!

RESTful처럼 지켜야되지만 지키기 쉽지 않은 원칙이라는 것은 확실한 것 같다. 하지만 모든 개발자들이 그렇듯 원칙을 지키기 위해 노력한다면 정말 좋은 코드를 만들 수 있을 것이라고 생각한다.

![](https://velog.velcdn.com/images/kimjiwonpg98/post/32635fa7-df6c-43c7-9c14-4a668000c343/image.jpg)




