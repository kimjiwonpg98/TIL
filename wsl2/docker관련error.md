
 ## 1. 상황
 
 - window에서 우분투 환경을 사용하는 wsl을 사용하고 있던 상황에 docker를 사용하게 되었습니다.
 - docker를 wsl2 기반으로 사용하도록 설정했을 때 **vmmem프로세스**가 사용된다는 것을 알게 되었습니다.
 🔮 vmmem 프로세스: hyper-v와 비슷한 가상 머신 플랫폼
 - 장치관리자로 본 결과 vmmem프로세스가 메모리의 49%나 차지하고 있었습니다.
 
 -----
 
## 2. MS에서 해결책은?
 
 - [github issue](https://github.com/microsoft/WSL/issues/4166)
 
 MS 측에서도 아직 해결법을 찾지 못해 이슈 오픈을 해둔 상태입니다.
 
 -----------
 
## 3. 문제의 원인
 
 #### 🤔 본질적인 원인
 
 1. 리눅스에서 파일 엑세스 할 때의 정보를 캐시로 사용하기 위해 메모리에 보존
 2. 이 과정은 메모리가 부족할 때까지 반복
 3. WSL2는 리눅스의 메모리 사용량에 따라 사용 메모리 크기를 **동적**으로 증가/감소
 
 - 여기서 중점은 동적으로 사용 메모리 크기를 늘리고 줄인다는 것입니다.
 
 ----------
 
## 4. 문제 해결 방안
 
 - 확실한 해결방안은 없지만 그래도 보편적으로 사용되고 있는 해결 방안에 대해 적어보겠습니다.
 
 ### 1. WSL2 사용 메모리 크기 강제 할당
 
 > C:\Users\사용자이름 폴더에 들어가 .wslconfig 파일을 생성
 
 
 #### .wslconfig 내용
 
 > [wsl2]
 memory=3GB
 swap=0
 
 memory 크기는 자신이 원하는 만큼 적어주시면 됩니다.
 
 
 ### 2. 원할때만 docker desktop 실행
 
 - 이 방법은 본질적인 해결방안은 아닌 것 같습니다.
 - 하지만 사용하지 않을때는 vmmem 프로세스가 사용되지 않으니 좋을 수 있습니다.
 
 Setting => General에서 StartDocker Desktop when you log in의 체크를 풀어주시면 됩니다.
 ![dockerImage](https://images.velog.io/images/kimjiwonpg98/post/8fa7d679-6c16-45d7-a6f4-2ed6fd40a3d4/docker.PNG)
 
 
 
 -----
 
 
 
 ### 느낀점
 
 여러가지 방법이 많았지만 이 고질적인 문제가 확실하게 해결되는 방법은 없었던 것 같다.
 확실히 window가 우분투도 사용하고 많이 좋아졌지만 짜잘한 문제가 많아서 안타깝지만 빨리 해결되었으면 좋겠다ㅎㅎ
 
 ---------
 
 
 ### 참고blog
 
 
 [참고 blog1](https://meaownworld.tistory.com/160)
 [참고 blog2](https://codeac.tistory.com/126)
 
 
 
 