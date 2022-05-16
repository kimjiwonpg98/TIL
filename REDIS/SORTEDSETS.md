# [Sorted Sets](http://redisgate.kr/redis/command/zsets.php)

## Init

기본적으로 redis는 key와 value값으로 구성되어있다.
하지만 sorted sets은 list로 되어있어 **key**하나에 **score**와 **value**로 구성이 된다.

sorted sets을 레디스에서는 zset이라고 말한다 이제 zset이라고 적겠다.


## 사용하는 경우

- 중복되는 member가 있을 때 업데이트가 용이하다.
- 여러 명령어가 준비되어 있어 사용하기 쉽다.

## [스킵 리스트 문서 파보기](http://redisgate.kr/redis/configuration/internal_skiplist.php)

sorted set은 내부적으로 두 가지의 구조로 저장한다.

레디스의 선택에 의해 데이터 구조를 선택한다.

1. 멤버 수로 선택! 

- 하나의 멤버 수가 128개까지는 zip list라는 데이터 구조에 저장
- 129개부터는 skip list에 저장한다.

2. 값의 길이로 선택

- 64byte까지는 zip list
- 65byte부터는 skip list

**🤔 두 가지 데이터 구조를 사용하는 이유는?**

레디스가 메모리 절약에 최적화된 memory DB라는 것을 다들 알고 있을 것이다. 
그 중에서도 zip list는 메모리 절약에 최적화된 구조다. 왜냐면 저장하는 데이터의 형태에 따라 길이에 맞게 최적화하여 저장하기 때문이다.
그리고 skip list는 zip list와 다른 역할을 한다.
정렬을 유지하면서 데이터를 삽입, 삭제하고 탐색하는 데이터 구조체다.


## skip list

기본적으로 redis는 링크드 리스트를 사용한다.

알고리즘 공부를 하다보면 알겠지만 링크드 리스트의 시간복잡도는 N으로 차례대로 값들을 비교하게 된다.

이부분을 포인터로 처리하였다.

그 설명은 위의 링크로 대신하기로 하자

설명을 읽었다는 가정하에 높은 레벨이 나오는 것을 방지하기 위해 redis는 **SPAN(순서)**이라는 필드를 두고 **레벨마다의 포인터를 저장**하여 탐색할 때 최적의 레벨을 사용할 수 있게 하였다.



