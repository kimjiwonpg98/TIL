# bcrypt (단방향 해시 함수 이용 모듈)

### bcrypt & salt

> bcrypt는 비밀번호를 암호화하기 위해서 사용
> salt와 bcrypt는 세트로 salt는 같은 문자열에 대해 다른 인코딩된 결과를 반환시켜 준다.

<br>

### SHA도 있는 데 bcrypt를 쓰는 이유

> SHA는 너무 빠른 것이 단점으로 => 길이의 한계와 하드웨어의 문제
> bcrypt는 Blowfish를 이용해 반복횟수를 정해 작업량(=해싱시간)을 조절가능

<br>

### 쓰는 방법

```js
//salt를 만드는 함수 genSalt
bcrypt.genSalt(rounds, (err, salt) => {
    //원래 비밀번호 + salt해서 hash를 만드는 함수
    bcrypt.hash(plainpassword, salt, 콜백 메서드)
})
```

**rounds는 반복횟수**

2021.03.03
