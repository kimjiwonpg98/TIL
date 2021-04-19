# 🧐 Component Exception 에러
-----


## 전체 에러 코드
-----
>Error: Element type is invalid: expected a string (for built-in components) or a class/function (for composite components) but got: undefined. You likely forgot to export your component from the file it's defined in, or you might have mixed up default and named imports.

## 해석
------
이 에러같은 경우는 라이브러리를 import할 때 없는 경우나
default export로 정의 되어있는데
import {라이브러리} from "~~"로 정의했을 경우 뜨는 에러


### 해결방법
-----
- 라이브러리를 선언할 때 중괄호 확인
- default로 정의되어 있을 경우 **import 라이브러리 from "~~"**로 선언 