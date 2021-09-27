### 생각보다 되게 간단하다.


- 외래키 검사를 끄고 삭제 후 다시 키면 된다.

```SQL
SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE TABLE_NAME;
SET FOREIGN_KEY_CHECKS = 1;
```
