# git 초기 설정 (불필요한 로그인 X)

```md
git config --global user.name "name"
git config --global user.email email

//git config 확인방법
git config --list

//wsl에서 사용시
git config --global credential.helper "/mnt/c/Program\ Files/Git/mingw64/libexec/git-core/git-credential-manager-core.exe"
```


[참고자료](https://docs.microsoft.com/ko-kr/windows/wsl/tutorials/wsl-git#git-credential-manager-setup)