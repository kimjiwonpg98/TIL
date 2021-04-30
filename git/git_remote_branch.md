# 🙄 원격 저장소의 브랜치를 가져와서 작업할 경우

## 1. git remote update
```
git remote update
```
update하게 되면 원격 저장소에 있는 브랜치로 checkout이 가능하다!

## 2. 확인방법
원격 저장소의 branch list 보는법
```
git branch -r
```
원격, 로컬 둘 다 보는 법
```
git branch -a
```

## 3. 원격 저장소의 branch 가져오기
```
git checkout -t origin/브랜치이름
```