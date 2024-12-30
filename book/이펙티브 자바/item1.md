## 생성자 대신 정적 팩터리 메서드를 고려하라

> 클래스의 인스턴스를 얻는 전통적인 수단은 public 생성자이다. 하지만 생성자 대신 정적 팩터리 메서드를 제공할 수 있다.

### 장점

- 생성자와는 달리 정적 팩터리 메서드는 이름을 가질 수 있다.
- 생성자와는 달리 호출할 때마다 새로운 객체를 생성할 필요가 없다.
- 생성자와는 달리 반환값 자료형의 하위 자료형 객체를 반환할 수 있다.
- 입력 매개변수에 따라 매번 다른 클래스의 객체를 반환할 수 있다.
- 정적 팩터리 메서드를 작성하는 시점에는 반환할 객체의 클래스가 존재하지 않아도 된다.

**이름을 가질 수 있다.**
- 생성자인 BigInteger(int, int, Random)와 정적 팩터리 메서드인 BigInteger.probablePrime과 BigInteger.valueOf를 비교해보자.

```java
public static void main(String[] args) {
    // 생성자 사용 예시
    BigInteger bi1 = new BigInteger(130, 10, new Random());

    // 정적 팩터리 메서드 사용 예시
    BigInteger bi2 = BigInteger.probablePrime(130, new Random());
    BigInteger bi3 = BigInteger.valueOf(12345L);

    System.out.println("bi1: " + bi1);
    System.out.println("bi2: " + bi2);
    System.out.println("bi3: " + bi3);
}
```

> 생성자를 사용할 때는 어떤 매개변수가 들어갈지 유추하기 힘들지만 정적 팩터리 메서드는 이름을 통해 어떤 역할을 하는지 유추할 수 있다.

**호출할 때마다 새로운 객체를 생성할 필요가 없다.**

- 말 그대로 생성자를 사용할 시 new 메서드를 이용해 새로운 객체를 생성함으로써 메모리를 잡아먹게 되는데 정적 팩터리 메서드를 사용할 시 이러한 문제를 해결할 수 있다.
- 불변 클래스는 인스턴스를 미리 만들어놓거나 캐싱해서 재활용하는 방식으로 불필요한 객체 생성을 피할 수 있다.

> 📝 인스턴스 통제 클래스 <br/>
> 클래스를 싱글턴, 인스턴스화 불가한 클래스로 만들어 같은 인스턴스는 항상 하나로 만듦으로써 e.equals(e)가 항상 true가 되도록 만들 수 있다.

**반환값 자료형의 하위 자료형 객체를 반환할 수 있다.**

- public이 아니더라도 그 객체를 반환할 수 있어 API를 더 유연하고 작게 만들 수 있다.


**입력 매개변수에 따라 매번 다른 클래스의 객체를 반환할 수 있다.**

- 반환 타입의 하위 타입이기만 하면 어떤 클래스의 객체를 반환하든 상관없다.
- 클라이언트는 그 클래스의 존재를 알 필요가 없어진다. (캡슐화)

**정적 팩터리 메서드를 작성하는 시점에는 반환할 객체의 클래스가 존재하지 않아도 된다.**

-  인터페이스를 반환 타입으로 사용하고, 실제 구현 클래스는 나중에 정의할 수 있고 이를 통해 더 유연한 설계가 가능해진다.


### 단점

- 상속을 하려면 public이나 protected 생성자가 필요하니 정적 팩터리 메서드만 제공하면 하위 클래스를 만들 수 없다.
- 정적 팩터리 메서드는 프로그래머가 찾기 어렵다.

**상속을 하려면 public이나 protected 생성자가 필요하니 정적 팩터리 메서드만 제공하면 하위 클래스를 만들 수 없다.**

- 제약을 걸기 위해서 상속보다는 컴포지션을 이용하고 불변 타입으로 만드는 것이 단점으로 받아들여질 수 있다.

**정적 팩터리 메서드는 프로그래머가 찾기 어렵다.**

- 생성자처럼 API 설명에 명확히 드러나지 않으므로 사용자는 정적 팩터리 메서드 방식을 인지하기 어려울 수 있다.
- 사용자는 정적 팩터리 메서드 방식 클래스를 인스턴스화할 방법을 찾아야 한다.

### 명명 방식들

- from: 매개변수를 하나 받아서 해당 타입의 인스턴스를 반환하는 형변환 메서드
  - ex) Date d = Date.from(instant);
- of: 여러 매개변수를 받아 적합한 타입의 인스턴스를 반환하는 메서드로 enumSet인 경우 사용하고 싶은 원소들을 매개변수로 받아 Set 인스턴스를 반환한다.
  - ex) Set<Rank> faceCards = EnumSet.of(JACK, QUEEN, KING);
- instance 혹은 getInstance: 매개변수로 명시한 인스턴스를 반환하지만, 같은 인스턴스임을 보장하지 않는다.
  - ex) StackWalker luke = StackWalker.getInstance(options);
- create 혹은 newInstance: instance 혹은 getInstance와 같지만, 매번 새로운 인스턴스를 생성해 반환함을 보장한다.
  - ex) Object newArray = Array.newInstance(classObject, arrayLen);
- getType: getInstance와 같으나, 팩터리 메서드가 다른 클래스에 속해 있을 때 사용한다.
  - ex) FileStore fs = Files.getFileStore(path);
- newType: newInstance와 같으나, 팩터리 메서드가 다른 클래스에 속해 있을 때 사용한다.
  - ex) BufferedReader br = Files.newBufferedReader(path);
- type: getType과 newType의 간결한 버전
  - ex) List<Complaint> litany = Collections.list(legacyLitany);


### 정리

- 정적 팩터리 메서드와 public 생성자는 각자의 쓰임새가 있으니 상황에 맞게 사용하자.

