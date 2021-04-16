# stack 내비게이션
<p>

## 필요한 라이브러리
>npm install @react-navigation/stack

## 👷‍♂️ 하는일
- 현재 화면 위에 다른 화면을 쌓으면서 화면을 이동
- 특정 항목의 상세 화면으로 이동할 때 많이 사용
![push&pop](https://user-images.githubusercontent.com/75289370/114828093-75e60a00-9e04-11eb-87e0-9b48ba3ef6cd.png)

------
## 사용방법
<br>

### 초기설정
```js
import { createStackNavigator } from "@react-natgation/stack";
//stack navigation 생성
const Stack = createStackNavigator();

//컴포넌트로 사용할 때
const StackNavigation = () => {
  return (
    <Stack.Navigator>
      <Stack.screen name="home" component={컴포넌트} />
    </Stack.Navigator>
  );
};
```
이렇게 하고 **NavigationContainer** 하위 컴포넌트로 들어간다.

> 순서 Stack.screen => Stack.Navigator => NavigationContainer

<br>

### 🕵️‍♀️ screen에서의 나오는 순서를 바꾸기 위해선 2가지 방법이 있다.
1. 컴포넌트의 순서를 변경한다.
2. <Stack.Navgator> 안에 initialRouteName="컴포넌트" 속성을 넣어주면 된다.

-------

### 화면 이동
1. Screen 컴포넌트의 component로 지정된 컴포넌트는 화면으로 이용
2. navigation이 props로 전달된다.

그래서 화면 이동은 Screen 컴포넌트의 component로 지정된 컴포넌트에서 설정
**navigation.navigate("원하는 화면 이름")**으로 사용!!

✨ 여기서 중요한 점은 원하는 화면 이름 자리에는 Screen 컴포넌트의 name 값 중 하나여야 한다.

### navigation.navigate() 사용 방법

```js
const List = {{ navigation }} => {
  const _onPress = item => {
    navigation.naivigate("Detail", {id: item._id, name: item.name});
  };

  //_onPress를 적당한 곳에 사용
};
```
전달받는 컴포넌트에서는 route의 params로 받음(example: route.params.id)

### 화면 전체를 차지하기 위해 사용하는 옵션
Stack.Navigator안에
```js
screenOptions={{cardStyle: {backgroundColor: "#ffffff"}}}
```

