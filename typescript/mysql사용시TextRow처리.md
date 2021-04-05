# mysql에서 query문 결과값 처리

query문에서 처리하는 부분은 RowDataPacket[]으로 처리된다.

ex)
```ts
 db.query(sql, [id], function (err, lists: RowDataPacket[]) {
 }
```
그래서 결과값이 여러 값이 나올 경우

```
[
  TextRow {
    num: 788,
    sellerId: 'test',
  },
  TextRow {
    num: 780,
    sellerId: 'test'
  }
]
```
이런식으로 TextRow값으로 나오게 된다.
<br>
하지만 typescript에서는 결과값을 interface나 type으로 결과값이 어떤 값이 나와야되는지 비교해야한다.

그래서 TextRow가 아니라 원시값으로 나올 수 있게 해주어야 한다.
```
[
  {
    num: 788,
    sellerId: 'test',
  },
  {
    num: 780,
    sellerId: 'test'
  }
]
```
이렇게

하려면

```ts
const 변수이름: 비교할interface[] = Object.values(
          JSON.parse(JSON.stringify(rows))
        );
```

rows을 문자열로 바꾼 후 다시 오브젝트로 바꿔줍니다. 그다음 Object.values를 이용해 배열로 만들어 줍니다.
