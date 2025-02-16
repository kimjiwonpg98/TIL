# REDIS 문자열 명령어

1. set
```
set key값 value값

ex) set key hello
set key2 "hello world"
```
set은 하나의 키와 하나의 값을 저장할 수 있습니다.

💫 응답: 항상 OK

2. append

```
append key "world"
```
2-1. 주어진 키값이 존재한다면 마지막에 값을 추가합니다.   
2-2. 키가 존재하지 않는다면 set과 동일하게 동작합니다.

💫 응답: 추가된 문자열 포함 전체 문자열 길이

3. get
```
get key값
```
key값에 맞는 value값을 응답합니다.

4. incr & decr
```
incr key값
decr key값
```
- incr은 value가 integer일 경우 숫자를 1씩 증가합니다.
- decr은 incr과 반대로 1씩 감소합니다.
- 결과값은 value값을 보여줍니다.