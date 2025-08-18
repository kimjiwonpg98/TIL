## 코루틴 시작

- 다른 멀티 스레드와 다른 점
  - 코루틴은 스레드 기반으로 동작하지 않는다.
  - 코루틴이라는 작업 단위를 사용함으로써 스레드의 사용 권한을 양보할 수 있다.

- runBlocking
  - runBlocking을 호출한 스레드를 사용해 실행되는 코루틴을 만든다.
    - runBlocking 코루틴이 종료될 때 스레드 점유도 해제하게 된다.
- 위에서 스레드의 사용 권한을 양보할 수 있다고 했는데
- 그건 launch 함수를 사용하면 된다.
  - launch는 항상 코루틴 스코프가 필요하다.


```kotlin
fun main() = runBlocking<Unit> {
    println("코루틴 시작")
    
    launch {
        println("코루틴 실행")
    }
}
```

- 코루틴 디버깅을 위한 방법
  - 설정하기

  - edit run configuration에서 **VM options** 을 설정

```
-Dkotlinx.coroutines.debug
``` 

 -  breaakpoint 사용하기


- 각 코루틴 이름 지어주기

```kotlin
fun main() = runBlocking<Unit>(CoroutineName("run Block 코루틴")) {
    println("코루틴 시작")
    
    launch(CoroutineName("launch 코루틴")) {
        println("코루틴 실행")
    }
}
```