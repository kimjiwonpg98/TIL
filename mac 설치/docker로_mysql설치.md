## 도커로 mysql 설치법

1. 도커를 먼저 설치    
   [공식홈페이지](https://docs.docker.com/desktop/install/mac-install/)에서 설치하거나 brew install docker로 설치
   - 설치 후 docker -v로 설치되어있는지 확인
     <br><br>
2. mysql 컨테이너 저장   
    ```docker pull --platform linux/amd64 mysql:8.0.28```
    - m1 & m2인 경우 Platform를 꼭 써주어야한다.
      <br><br>
3. mysql 컨테이너 실행    
    ```docker run --platform linux/amd64 --name mysql -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=비밀번호 mysql:8.0.28```
    - 초기 비밀번호와 함께 docker 실행
<br><br>
4. mysql 컨테이너에 접속   
   ```docker exec -it mysql bash```
    - name으로 정해둔 이름으로 접속
    - .zshrc에 alias로 단축어 만들어 두면 편함

### ** 주의사항
   mysql 설치 시 버전 꼭 적어주길바람
   버전을 기재하지 않을 시 apt-get 불가능..