# 전체 앱을 총괄하는 내비게이션
<p>

## 구성요소

1. NavigationContainer 컴포넌트
2. Navigator 컴포넌트
3. Screen 컴포넌트

![화면](https://user-images.githubusercontent.com/75289370/114808917-2a236880-9de4-11eb-988e-3bed67b8de93.png)

### 🎨 Screen 컴포넌트
- 화면으로 사용되는 컴포넌트
- name과 component 속성을 지정해줘야 한다.
  - name은 화면 이름
  - component 화면으로 사용될 컴포넌트를 전달
- 항상 navigation과 route가 props로 전달

### 👷‍♂️ Navigator 컴포넌트
- 화면을 관리하는 중간 관리자 역할
- 내비게이션을 구성, 여러 개의 Screen 컴포넌트를 자식 컴포넌트로 갖고 있다.

### 👨‍💻 NavigationContainer 컴포넌트
- 네비게이션의 계층 구조와 상태를 관리하는 컨테이너 역할
- 모든 내비게이션 구성 요소를 감싼 **최상위 컴포넌트!**

### 설정 우선 순위
- 우선순위는 Screen > Navigator > NavigationContainer 로 적은 범위일수록 우선순위가 높다.


### 설치 해야할 라이브러리
> npm i --save @react-navigation/native

리액트 내비게이션은 각 기능별로 모듈이 분리되어 있어 개별적으로 추가 라이브러리를 설치해야 한다.
- expo일 경우
> expo install react-native-gesture-handler 
> react-native-reanimated 
> react-native-screens 
> react-native-safe-area-context 
> @react-native-community/masked-view
expo가 아니라면 npm or yarn

