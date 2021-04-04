# TYPESCRIPT 쓰는 방법

1. tsconfig.json 생성

ts를 js로 변환시켜주는 tsc를 호출하면 상위 폴더의 tsconfig.json를 검색하기 때문에 먼저 만들어주도록 한다.

```json
{
  "compilerOptions": {
    "module": "commonjs",
    "target": "ES5",
    "sourceMap": true,
    "outDir": "./dist",
    "strict": true
  },
  "compileOnSave": true,
  "buildOnSave": true,
  "include": ["src/**/*"],
  "exclude": ["node_modules"]
}
```
## compilerOptions(생략 가능)
module: 빌드 결과 모듈 방식
target: js로 변환 했을 때의 버전 방식
sourceMap: .map.js파일도 함께 생성
outDir: 빌드 결과물 폴더 지정

### 여기 안써놨지만 있는 옵션들

lib: 라이브러리형식(Array)
allowJS: JS 파일도 컴파일 대상에 포함(Boolean)
rootDir: 컴파일할 대상들이 들어있는 폴더
noUnusedLocals: 사용안하는 로컬 변수가 있으면 에러 처리(Boolean)

## include

컴파일에 포함되는 파일 경로 지정
<br>
없다면 지원하는 확장자 파일 모두 포함

## exclude

컴파일에 포함되지 않는 파일들 지정

2. typescript에 필요한 라이브러리 설치

* typescript
* tsc AND tsc-watch
* ts-loader

**주의사항** npm i --save-dev로 까는것이 좋음

npm 홈페이지 들어가서 ts를 지원하는지 확인 후
지원하지 않는다면 @types/library로 설치



2021/04/03
