# ssh키 생성

## 만드는 이유
git push 시 아이디와 비밀번호 쓰는 번거로움을 없애기 위해서 만든다.

1. cd ~
2. ssh-keygen 후 Enter키
3. cd ~/.ssh
4. ls -al로 id_rsa와 id_rsa.pub있는지 확인
5. cat id_rsa.pub로 퍼블릭키 확인 후 복사

|비공개키|공개키|
|--|--|
|id_rsa|id_rsa.pub|

6. git의 setting으로 이동
7. SSH and GPS keys에서 New SSH Key
8. 복사한 값 입력 후 생성