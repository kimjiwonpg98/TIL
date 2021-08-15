# 🧐 JMETER란?

- 풀네임은 Apache Jmeter이고 서버가 제공하는 서비스에 대한 성능을 측정하고 보여주는 테스트 도구입니다.
- 서버에 많은 요청을 보내서 어느정도까지 버틸 수 있는지 확인하기 좋은 도구입니다.


# 💻 JMETER 설치

### 1. 🕵️‍♀️ 설치방법

- window 기준

http://jmeter.apache.org/download_jmeter.cgi (다운로드 링크)

들어가서 Binaries의 zip파일을 다운받아 압축을 풀어주면 됩니다.

푼 후에 bin 폴더의 jaz파일을 실행하면 되는데 실행되지 않는다면 window 배치파일을 실행시켜주세요

🧐 주의할 점: jmeter는 java로 실행되기 때문에 java 버전 8이상이 설치되어야합니다.

------

### 2. 📖 사용방법

1. Test Plan에서 add > Threads > Threads Group
- **Thread Group 화면**
![쓰레드](https://images.velog.io/images/kimjiwonpg98/post/37383f98-dee9-4aa5-aa89-ffbb7fadffb7/%EC%93%B0%EB%A0%88%EB%93%9C%EA%B7%B8%EB%A3%B9.PNG)
- **Number of Threads(users)** 
    사용자를 몇 명으로 설정할 것인지 대한 값입니다. (사용자 = 쓰레드)
- **Ramp-up Period(in seconds)**
    한번의 실행을 몇초 동안 완료 시킬것인지에 대한 설정값입니다.
- **Loop Count**
    한 사용자가 몇 번 반복하는지 설정하는 값 (Infinite는 무한)

2.  Threads Group에서 add > Sampler > Http Request
- **Http Request 화면**
![HTTTP Request](https://images.velog.io/images/kimjiwonpg98/post/8baa8bac-5b0c-4527-a824-0d898d0fabed/httprequest.png)

- **Protocol (http)**
    - 기본 값 http, https라면 https를 적어줍니다.
    - 자신의 서버 프로토콜을 적어주면 됩니다.
- **Server Name or IP**
    - 서버의 DNS Name이나 IP를 적어줍니다.
- **Port Number**
    - 기본값은 80
    - 자신의 포트 번호를 적어줍니다.
- **HTTP Request**
    - 자신이 테스트할 HTTP Request를 지정합니다.
- **Path**
    - 자신이 테스트할 주소를 적어줍니다.
    
3. run

- 위 화면의 재생 표시를 클릭하면 실행됩니다.

4. 확인 방법

- 자신이 원하는 곳 > Add > Listener > View Results Tree
- 자신이 원하는 곳 > Add > Listener > Summary Report

- 자신이 원하는 곳: Http Request or Thread Group

![View Result](https://images.velog.io/images/kimjiwonpg98/post/5fd3415e-0e79-4dc2-9938-087760cec3d9/viewdetail.png)

![Summery](https://images.velog.io/images/kimjiwonpg98/post/21e9ce60-b056-4c5b-bd9b-9dc6303a877b/summery.png)

-----

### 결론

자신이 만든 서버의 트래픽을 간단하게 테스트하기에 좋은 도구라고 생각됩니다.
꼭 개발서버에서 하시길!!

------

### 참고

- [블로그](https://hayden-archive.tistory.com/398)

