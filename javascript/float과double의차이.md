# float과 double의 차이점

- 기본적으로는 두 data-type 모두 실수를 표현하기 위해 사용하는 자료형이다.
- 차이점이라고 묻는다면 float은 4Byte, double은 8byte라는 점? 이라고 다들 말할 것이다.

하지만 여기서 중요한 점은 `정밀도`이다

![type](https://user-images.githubusercontent.com/75289370/158063253-5d2bd5b6-0a88-4416-9b2c-9e3288603d98.png)

> 위의 그림에서 유효자릿수가 정밀도를 뜻하게 된다.
정확하게 말해서 몇자리까지 오차없이 표현할 수 있는가를 나타낸다.

- float은 7자리
- double은 15~16자리

> 단일-정밀도 형식: 32비트로 표현된 부동소수점 수 (float)
복수-정밀도 형식: 64비트로 표현된 부동소수점 수 (double)


## 실수형의 저장 방식

float와 double은 부호, 지수, 가수로 나눠서 표현하게 된다.

- 부호: 0이면 양수, 1이면 음수
- 지수: 부호있는 정수
- 가수: 실제 값을 저장하는 부분

314,000,000,000,000은 3.14 x 10^14으로, 0.00000000000314는 3.14 x 10^-12로 표현할 수 있다. 여기서 소수점의 위치를 지수로 표현할 수 있다.

예시에서는 14와 -12가 지수가 된다.





