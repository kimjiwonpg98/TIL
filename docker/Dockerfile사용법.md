# Dockerfile사용법

```
FROM project:1.1.0

ENTRYPOINT ["echo", "hello"]
```

- FROM은 새로운 이미지를 생성할 때 기반으로 사용할 이미지를 지정 
- ENTRYPOINT는 컨테이너를 시작할 때 실행할 명령어를 입력

## docker build

- docker build 명령어로 이미지를 생성할 수 있습니다.

```
docker build --tag echohello:1.1.0 .
```

- --tag 혹은 -t 옵션은 새로 생성할 이미지를 지정합니다.
- 저장소 이름으로 echohello를 하고 태그는 1.1.0으로 사용했습니다.
- 마지막 . 은 Dockerfile의 위치를 지정합니다.