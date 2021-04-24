# 데이터 추가 INSERT

```sql
INSERT INTO  table_name(field1, field2) VALUES (data1, data2)
-- 전체를 할때
INSERT INTO  table_name VALUES (data1, data2)
```

필드의 이름을 생략할 수 있는 경우가 있다.

1. Null이 저장 가능하게 설정한 필드
2. DEFAULT 제약 조건이 있는 필드
3. AUTO_INCREMENT가 설정된 필드
4. DATE 관련 필드

