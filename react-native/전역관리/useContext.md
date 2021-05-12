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

함수 자체를 넣게 되는 경우는 그안에 useState를 이용해 여러 컴포넌트에서 값을 변경할 수 있다.
<br>
하지만 Provider로 자식 컴포넌트로 감싼 컴포넌트만 가능하다.

ex)

```js 
const ReadyContext = createContext({
  isReady: false,
  dispatch: () => {},
});

const ReadyProvider = ({ children }) => {
  const [isReady, setIsReady] = useState("");

  const readyDispatch = {
    ready: () => setIsReady(true),
    notReady: () => setIsReady(false),
  };

  const value = { isReady, readyDispatch };

  return (
    <ReadyContext.Provider value={value}>{children}</ReadyContext.Provider>
  );
};
```
 다른 파일에서

 ```js
import { ReadyContext } from "../Context";

const { isReady, dispatch } = useContext(ReadyContext);

dispatch.ready() // true로 변환

console.log(isReady) // true
 ```
이렇게 사용