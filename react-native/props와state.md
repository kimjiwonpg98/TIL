# 📖 props와 state

## 🧐 props

**부모 컨포넌트로부터 전달받은 속성값 혹은 상속받은 속성값**

💡 부모가 자식의 props를 설정하면 자식은 해당 props를 사용할 수 있지만 **변경은 불가능**하다.

1. 부모 컨포넌트에서 ```<Button title="Button" />``` 속성을 준다.
2. 자식 컨포넌트에서 속성을 받는다. ```const button = props => {}```
3. {props.title} 이런 식으로 사용한다.

### 📃 default props
값이 정해지지 않았을 때 props의 기본값을 정해준다.
ex)
```js
Btn.defaultProps = {
  title: "Button",
};
```
### 📃 proptypes
props 전달시 잘못된 타입을 전달하거나 필수로 전달해야 되는 값이 가지 않을 경우가 있을 수 있다.
그래서 proptypes를 이용해 타입이나 필수 여부를 정해준다.

ex)
```js
Btn.propTypes = {
  title: PropTypes.string.isRequired,
  onPress: PropTypes.func.isRequired,
};
```




## 🧐 state

**state는 props와 반대로 컴포넌트 내부에서 생성되고 값도 변경 가능하다.**

그래서 컴포넌트에서 변화할 수 있는 값을 모두 state라고 부른다.

Hooks를 이용해 함수형 컴포넌트에서 상태를 관리할 수 있다.