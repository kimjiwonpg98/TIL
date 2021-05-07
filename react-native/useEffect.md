# 렌더링마다 작업 실행하는 useEffect

```js
useEffect(() => {}, []);
```
1. 첫번째 파라미터인 함수는 조건을 만족할 때마다 호출
2. 두번째 파라미터인 배열은 함수가 호출되는 조건을 설정

예를 들어 어떤 값이 변경되었을 때 useEffect안의 함수를 호출하는 식으로 사용

- 두번째 파라미터인 배열에 빈 배열을 전달하면 처음 렌더링될 때 함수가 호출
- 첫번째 파라미터에 return값에 함수를 반환하면 언마운트될 때 실행 (배열도 빈 배열이여야 함!)

✨ 전달하는 함수에서 반환을 함수로 하는 것을 **정리함수**라고 한다!