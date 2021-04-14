# Consumer 컴포넌트를 대체한 Hook
<p>

✨ useContext 함수는 Consumer 컴포넌트의 자식 함수로 전달되던 값과 동일한 데이터 반환

```js
import React, { useContext } from 'react';
import UserContext from "../~~";

const { user } = useContext(UserContext);
//UserContext: createContext함수
```
Consumer 컴포넌트는 자식으로 반드시 컴포넌트를 반환하는 함수를 넣어야 하지만
<br/>
useContext는 함수 자체를 넣어도 괜찮다.
