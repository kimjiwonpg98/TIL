## coroutine dispatcher

- dispatch (보내다) + er (주체) = 보내는 주체
  - 코루틴을 스레드로 보내 실행시키는 객체

> 일반적인 dispatcher는 작업 대기열을 가지고 있어 사용할 스레드 풀로 보내준다.

single

```kotlin
val singleThreadDispatcher: CoroutineDispatcher =
    newSingleThreadContext("singleThread")

fun main() = runBlocking<Unit> {
  launch(singleThreadDispatcher) {
    println("${Thread.currentThread().name} 실행")
    // singleTread 실행
  }
}
```

multi

```kotlin
val multiThreadDispatcher: CoroutineDispatcher =
    newFixedThreadPoolContext(2,"mutliThread")

fun main() = runBlocking<Unit> {
    launch(multiThreadDispatcher) {
        println("${Thread.currentThread().name} 실행")
        // mutliThread-1 실행
    }
    launch(multiThreadDispatcher) {
        println("${Thread.currentThread().name} 실행")
      // mutliThread-2 실행
    }
}
```

이렇게 `newFixedThreadPoolContext` 같이 컨텍스트를 미리 만들어서 사용하는 건 위험할 수 있다.
- 이유: 미리 스레드 풀을 점유하고 시작하기 때문에 다른 작업에 영향이 갈 수 있다.


> 그래서 코루틴에서 미리 정의된 dispatcher를 사용해야 한다.

1. Dispatchers.IO

- 입출력(네트워크 요청이나 DB 읽기 쓰기 등) 작업을 실행하는 디스패처
  - 기본적으로 64와 JVM에서 사용할 수 있는 프로세서의 수 중 큰 값

```kotlin
fun main() = runBlocking<Unit> {
    launch(Dispatchers.IO) { // 부모
        launch { // 자식 1
            println("${Thread.currentThread().name} 실행")       
        }
        launch { // 자식 2
            println("${Thread.currentThread().name} 실행")
        }
    }
}
```
- 자식들의 dispatcher가 설정되지 않으면 부모의 dispatcher를 사용한다.

2. Dispatchers.Default

CPU 바운드 작업을 위한 디스패처
- 끊이지 않고 연산이 필요한 작업(이미지, 동영상 처리, 대용량 데이터 변환 등)

```kotlin
fun main() = runBlocking<Unit> {
    launch(Dispatchers.Default) { // 부모
        launch { // 자식 1
            println("${Thread.currentThread().name} 실행")       
        }
        launch { // 자식 2
            println("${Thread.currentThread().name} 실행")
        }
    }
}
```


### 공유 스레드풀
- 어떤 종류의 dispatchers 든 공유 스레드풀을 사용한다.

### limitedParallelism
- 동시에 실행할 수 있는 최대 코루틴(스레드) 수를 제한하는 기능
- Dispatcher.Default
  - 본인에게 **할당되어 있던 공유 스레드풀 안에서 그룹**을 만들어 제한  
- Dispatcher.IO
  - 본인이 할당하고 있는 스레드가 아니라 **공유 스레드풀의 새로운 스레드 풀 집합**을 만듦
  - 다른 작업에 방해 받지 않아야 하는 중요 작업이 있을 때 사용해야 함


3. Dispatchers.Main

- 메인 스레드에서의 작업을 위한 디스패처
- 안드로이드 코루틴 라이브러리 추가가 필요하다고 함








