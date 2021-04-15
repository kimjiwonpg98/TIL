# 🔗 branch에 관련된 명령어


## git bash에서의 branch
--------
### branch 확인

1. 현재 있는 branch 확인
> git branch
2. 원격 저장소 branch 확인
> git branch -r
3. branch 마지막 커밋 메시지 확인
> git branch -v
---------
<br>

### branch 생성 및 이동
1. branch 생성
> git branch 생성할 branch이름
2. 생성한 branch 이동
> git checkout branch이름
3. 생성 후 바로 이동
> git checkout -b branch이름
------------
<br>

### branch 삭제
> git branch -d branch이름
--------
<br>

### 생성한 branch를 git페이지에 있는 repo에 push하기
<br>

로컬에 있는 branch로 작업을 한 후 원격 repo에 올려야하는데 repo에는 관련된 branch가 없을 때 사용한다.

**즉 github페이지에는 없는 branch를 새로 팔 때 사용!**
>git push --set upstream origin 생성할 branch

>줄여서 git push -u origin 생성할 branch