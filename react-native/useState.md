# 컴포넌트 상태를 관리하는 useState
<p>

## 😎 사용하는 방법 2가지

----
<br>

1. 첫번째 방법

ex)
```js
import React, { useState } from 'react';

const [state, setState] = useState(초기값);

setState(state + 1);
```
- state: 변수이름
- setState: 변수를 수정하는 세터 함수
- 상태가 변경되면 컴포넌트가 변경된 내용을 반영
- 그 후 다시 렌더링된다.


2. 두번째 방법

>세터함수에 함수에 변경될 값을 전달한 첫번째방법과 다르게 세터 함수의 파라미터에 함수를 전달하는 방법

ex)
```js
import React, { useState } from 'react';

const [state, setState] = useState(초기값);

setState(prevState => {});
```
- 변경되기 전의 상태 값이 파라미터로 전달
- 그 값을 받아서 어떻게 수정할지 정의해주면 된다.
- 세터 함수는 **비동기**로 동작하기 떄문에 변경이 여러번 일어나게 되면 변경 전에 다시 업데이트가 실행된다.
- 그래서 차례대로 동작하게 하여 업데이트가 안되는 상황을 방지한다.