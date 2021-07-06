# Big O

> 시간 복잡도를 설명할 때 사용하는 개념

## O(1)

ex)
```py
def sort_func(arr):
  print(arr[0])
```
input size가 커져도 상관없이 시간복잡도는 O(1)

## O(N)

ex)
```py
def sort_func(arr):
  for i in arr:
    print(i)
```
커지면 커질수록 높아지기 때문에 O(N)으로 표현

루프안에서 실행되면 n^2

## O(logN)

ex)
이진 검색같이 나눠서 계산할 때 사용

