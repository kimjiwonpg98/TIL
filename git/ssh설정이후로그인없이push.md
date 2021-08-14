# ssh 설정 이후에도 로그인없이 push


## 1. 상황
- ssh 설정을 했음에도 wsl에서 로그인을 계속 하는 상황이 발생

## 2. 해결방안

### 1. 일단 git과 연결되어 있는지 확인

> ssh -T git@github.com

이렇게 했을 경우

> Warning: Permanently added the RSA host key for IP address '140.82.132.15' to the list of known hosts.
Hi jiwonpg98! You've successfully authenticated, but GitHub does not provide shell access

경고가 뜨지만 무시하고 ssh URL을 재정의해줍니다.


### 2. ssh URL 재정의

> git remote set-url origin git@github.com:<repo-url>.git

- 😎 예시

> git remote set-url origin git@github.com:kimjiwonpg98/TIL.git


------  
이렇게 하면 더이상 사용자 이름과 암호를 입력하지 않아도 됩니다!!