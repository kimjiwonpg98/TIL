# 🛒 lambda 표현식

## lambda를 사용하는 방법
> 표현식일 때: lambda 인자 : 표현식
> 함수일 때: lambda 매개변수 : 결과


## 정렬
--------
### 1. sorted
```py
strings = list["sun", "bed", "car"]
n = 1
def sort_func(strings, n):
  new_strings = sorted(strings, lambda x: x[n]);

  print(new_strings)
  # ["car", "bed", "sun"]
```
key 위치인자에 함수를 보내 함수에서 지정한 결과값에 따라 정렬을 한다.
<br>

lambda를 쓰게 되면 **list**안의 n번째 문자에 따라 정렬이 되게 된다.

### 2. map
map은 **map(함수, 리스트)**로 사용
```py
list(map(lambda x : x ** 2, range(5)))
# [0, 1, 4, 9, 16]
```
함수를 lambda로 받고 리스트를 range(5)로 받아 리스트를 반환해줍니다.

### 3. reduce
reduce는 **reduce(함수, 순서형 자료)** <br>
reduce는 원소를 차례로 적용시키는 함수입니다.

```py
from functools import reduce

reduce(lambda x, y: x + y, [1,2,3,4,5])
# 결과값: 15
```
### 4. filter
filter은 **filter(함수, 리스트)**로 사용
특정값을 걸러주는 역할을 한다.

```py
list(filter(lamdba x: x > 5, range(10)))
# [6,7,8,9]
```

## 익명함수 만들기
-------
기존 함수
```
함수이름(매개변수):
  return 결과
```

lambda 함수
```
lambda 매개변수: 결과
```
sorted 함수에서 사용한 lambda도 익명함수를 이용한 것이다.

```py
(lambda x : x + 1)(5)
# result: 6
```
이런식으로 바로 실행 함수를 만들 수도 있다.