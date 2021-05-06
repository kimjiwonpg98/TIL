# Encountered two children with the same key

## 이유
react에서는 동일한 키를 가지게 되면 반응 순환이 잘못되어 경고가 뜨게 됩니다.

## 해결방법

rendering되는 키의 값을 고유의 값으로 겹치지 않게 해주면 된다.