# 📖 reverse AND reversed

## reverse
-------

reverse는 list타입에서 제공하는 함수로 위치를 반대로 해준다.

**값을 반환하지 않는다.** 단순히 list안의 값만 바꿔준다.

```py
test  = [1, 2, 3]
test_reverse = test.reverse()

print(test_reverse) #None
print (test) #[3, 2, 1]
```

## reversed
-------

내장함수로 list에서만 사용하는 함수가 아니다.

**but 딕셔너리는 지원 X**

```py
test  = [1, 2, 3]
test_tuple = (1, 2, 3)
test_word = "abc"

reversed(test) # <list_reverseiterator object at 0x000001C48E44E940>
reversed(test_tuple) #<reversed object at 0x000001C48E44E940>
reversed(test_word) #<reversed object at 0x101053c10>
```
reversed 객체를 반환한다.

- join으로 list를 문자열로 바꿀때
```py
test = ["I", "am", "groot"]
" ".join(reversed(test)) #I am groot
```


## 파이썬답게 문자열 거꾸로 만들기
----- 
```py
test = "abcd"
print(test[::-1]) #dcba

print(test[2:0:-1]) #cb
# 2번째 인덱스부터 1번까지 역순으로 출력
```

결론적으로 [: : 1 or -1]
<br>
1. 첫번째 파라미터는 시작하는 인덱스
2. 두번째 파라미터 + 1이 끝나는 인덱스
3. 1이면 순서대로 -1이면 역순