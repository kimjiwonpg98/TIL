# commit에 관련된 이슈 정리

## 이슈 정리 전 개념 정리

1. 스테이징(staging): 확장할 변경 사항을 준비 (git add)
2. 인덱스 (Index): 확정될 준비가 된 변경 사항들이 모인 영역 (git add 후)
3. 헤드 (HEAD): 작업 중인 브랜치의 선두를 가리키는 포인터 이 헤드를 이용해 디텍터리의 상태를 바꿀 수 있다.

### 스테이징 취소 (git add 취소)

```md
// 파일 정해서 취소
git reset 파일명

//전체 취소
git reset
```

### 마지막 커밋 취소

```md
git reset --soft HEAD^
```

**--soft**는 작업 디렉토리와 인덱스를 보존해 스테이징 상태를 유지
**HEAD^** 는 헤드의 직전 위치

### 마지막 커밋 메시지 수정

```md
git commit --amend -m "message"

//길게 쓸 때
git commit --amend
```
git commit --amend를 하게 되면 nano 설정으로 들어가게 된다.

## 이미 푸시한 커밋 메시지 수정

```md
git rebase -i
//text editor가 나오면서 과거의 commit명이 나온다.
//ex)
pick 3543cdf Add(jiwon/User): message~
pick fdf32sv Refactor(jiwon/User): message~

//수정하려는 커밋의 pick을 edit혹은 e로 바꾼후 저장

git commit --amend -m "message"
git rebase --continue
git push -f origin branch
```
-f로 하기 때문에 강제로 과거 커밋 이력이 바뀌게 된다.
**협업하는 상황이면 사전 협의 필수!**

## 커밋 과거로 되돌리기

git reflog로 해쉬 확인

```md
git reset --hard 해쉬
```

## push한 커밋 과거로 되돌리기

git reflog로 해쉬 확인

```md
git revert 바꾸는 처음 해쉬...해쉬
Revert "메시지"
```


참고자료: https://parksb.github.io/article/28.html

2021.03.29