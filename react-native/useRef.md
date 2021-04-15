# DOM 선택 함수 역할하는 useRef
<p>

```js
import React, { useRef } from "react";

const ref = useRef(초기값);
```
react에서는 querySelector같은 DOM Selector함수 대신 useRef를 사용한다.

## 💫여기서 주의할 점!
---
1. ref로 지정하게 되면 생성된 변수에 값이 저장되는 것이 아니라 변수의 .current 프로퍼티에 해당 값을 담게 된다.

2. useState와 달리 useRef의 내용이 바뀌어도 다시 렌더링되지 않는다.

## 🧐 사용방법
---
1. 먼저 **const 변수 = useRef();** 로 ref 설정
2. 컴포넌트 안에서 **ref={변수}** 나 **변수.current.focus();** 로 포커스를 맞춘다.


### 참고
---
1. 컴포넌트 안에서 returnKeyType를 선언하면 키보드의 버튼을 바꿀 수 있다.

> "done": 완료버튼 <br> "next": 다음버튼

2. onSubmitEditing을 사용하여 current.focus를 바꿔주면 포커스를 이동시킬 수 있다.


