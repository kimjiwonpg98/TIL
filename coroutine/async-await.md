## async/await와 Deferred

### async vs launch 차이점
| 구분 | launch | async |
|------|--------|-------|
| **반환 타입** | Job | Deferred<T> |
| **결과 반환** | 불가능 | 가능 |
| **사용 목적** | Fire-and-forget | 결과가 필요한 작업 |

### Deferred 객체
```kotlin
// Deferred는 Job을 상속받음
interface Deferred<out T> : Job {
    suspend fun await(): T  // 결과 대기 및 반환
    fun getCompleted(): T   // 완료된 결과 즉시 반환 (완료 안되면 예외)
}
```

### async 사용 예시
```kotlin
// 1. 단일 async 작업
val deferred = async {
    delay(1000)
    "결과 데이터"
}
val result = deferred.await()  // "결과 데이터"

// 2. 병렬 처리
val deferred1 = async { fetchUserData(1) }
val deferred2 = async { fetchUserData(2) }

val user1 = deferred1.await()  // 첫 번째 결과 대기
val user2 = deferred2.await()  // 두 번째 결과 대기
```

### async 취소 처리
```kotlin
val deferred = async {
    try {
        delay(5000)
        "완료"
    } catch (e: CancellationException) {
        "취소됨"
    }
}

delay(1000)
deferred.cancel()  // async도 취소 가능

try {
    val result = deferred.await()  // CancellationException 발생
} catch (e: CancellationException) {
    println("async 작업이 취소됨")
}
```

### 예외 처리 차이점
```kotlin
// launch: 예외가 즉시 전파됨
val job = launch {
    throw Exception("에러 발생")  // 즉시 크래시
}

// async: await 호출 시점에 예외 전파
val deferred = async {
    throw Exception("에러 발생")  // 아직 크래시 안됨
}

try {
    deferred.await()  // 여기서 예외 발생
} catch (e: Exception) {
    println("예외 처리: ${e.message}")
}
```

### awaitAll 사용
```kotlin
// 여러 async 작업을 한번에 대기
val results = awaitAll(
    async { fetchData(1) },
    async { fetchData(2) },
    async { fetchData(3) }
)
// 모든 작업 완료 후 결과 리스트 반환
```
- async는 결과가 필요할 때만 사용, 단순 실행은 launch 사용