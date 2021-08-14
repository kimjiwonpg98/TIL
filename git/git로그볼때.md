## 1. git log

- commit했던 log의 전체적인 내용 모두를 보여줍니다.

## 2. git reflog

- commit했던 log를 메시지와 간단하게 보여줍니다.
- 돌아가려면 HEAD@{n}을 찾아서 ```git reset --hard HEAD@{n}```하면 됩니다.

## 3. git log -p -1

- -p 옵션은 각 커밋의 diff 결과를 보여줍니다.
- -1자리에 -2를 넣으면 최근 두 개의 결과만 보여줍니다.