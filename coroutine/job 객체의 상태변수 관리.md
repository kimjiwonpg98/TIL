## Job 객체 상태 변수 관리

| 상태 | isActive | isCompleted | isCancelled | 설명 |
|------|----------|-------------|-------------|------|
| **New** | false | false | false | 생성되었지만 아직 시작되지 않음 |
| **Active** | true | false | false | 실행 중인 상태 |
| **Completing** | false | false | false | 완료 처리 중 (자식 Job 대기) |
| **Completed** | false | true | false | 정상 완료된 상태 |
| **Cancelling** | false | false | true | 취소 처리 중 |
| **Cancelled** | false | true | true | 취소 완료된 상태 |

### 상태 전환 예시
```kotlin
val job = launch {  // New → Active
    delay(1000)
    println("작업 완료")  // Active → Completing → Completed
}

// 상태 확인
println("isActive: ${job.isActive}")        // true
println("isCompleted: ${job.isCompleted}")  // false
println("isCancelled: ${job.isCancelled}")  // false

job.cancel()  // Active → Cancelling → Cancelled
```

### 상태별 동작
- **New**: `start()` 호출 전까지 대기
- **Active**: 실제 코루틴 코드 실행
- **Completing**: 자식 Job들의 완료 대기
- **Completed**: `join()` 호출시 즉시 반환
- **Cancelling**: 취소 처리 및 정리 작업 수행
- **Cancelled**: 모든 정리 작업 완료
