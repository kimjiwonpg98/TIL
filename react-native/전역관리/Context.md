# 전역적으로 상태를 관리하는 Context API
<p>

- 기본 컴포넌트는 여러개의 컴포넌트를 걸쳐서 받아옵니다.
- 그럼 여러 컴포넌트가 있다면 과정에 속한 모든 컴포넌트를 찾아 수정해야 합니다.

## createContext
Context를 생성하는 함수
```js
const Context = createContext(defaultValue);
```

### 🔗Consumer 컴포넌트
<br>

- 상위 컴포넌트 중 가장 가까운 곳에 있는 **Provider 컴포넌트가 전달하는 값**을 사용
- 기준은 Consumer
- Provider 컴포넌트가 없다면 **createContext의 기본값**을 사용
- Consumer안에 있는 반환값(자식)은 반드시 리액트 컴포넌트를 반환하는 함수여야 한다.
```js
<UserContext.Consumer>
  {value => <StyledText>{value.name}</StyledText>}
</UserContext.Consumer>
```
- 반환하는 함수는 **현재값을 파라미터로 받아 사용가능**하다.
<br><br>

### 🔗Provider 컴포넌트
- 하위 컴포넌트에 Context의 변화를 알리는 역할을 한다.
- value를 받아 모든 하위 컴포넌트에 전달
- 그 하위 컴포넌트는 value가 변경될 때마다 다시 렌더링된다.
- **Consumer 컴포넌트를 감쌌을 때 value를 지정해 줘야한다.**

✨ 즉 value를 바꿔서 전달해주는 역할을 한다! ✨ 

Consumer 컴포넌트의 상위 컴포넌트에 Provider가 없어도 동작되도록 기본값의 형태는 createContext와 Provider가 동일하게 맞추는 것이 좋다.