## 👨‍💻 설치

> npm i --save-dev typescript eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin

## 1. typescript-eslint

- .eslintrc.json 파일 설정

```json
{
  "parser": "@typescript-eslint/parser",
  "parserOptions": {
    "project": "./tsconfig.json"
  },
  "env": {
    "node": true
  },
  "extends": ["plugin:@typescript-eslint/recommend"]
}
```

extends 설정을 이용해 eslint플러그인 적용하면서 recommend 규칙을 확장한다.

## 2. typescript-eslint 실행

터미널 기준
```
npx eslint --ext .js, .ts src

npx eslint src/**/*
```

VSCode 기준
ESLint 확장프로그램으로 설치하고

```json
{
  "eslint.validate": [
    { "language": "typescript", "autoFix": true },
    { "language": "typescriptreact", "autoFix": true }
  ]
}
```
설정에서 이 설정을 추가해준다.


## 3. prettier 함께 사용하는 법

- npm 설치

> npm i --save-dev prettier eslint-plugin-prettier eslint-config-prettier

- .eslintrc.json 설정에 추가

```json
{
  "extends": ["plugin:prettier/recommended", "prettier/@typescript-eslint"]
}
```

- **plugin:prettier/recommended**: eslint-plugin-prettier + eslint-config-prettier 동시 적용
- **prettier/@typescript-eslint**: prettier 규칙과 충돌하는 @typescript-eslint/eslint-plugin 규칙 비활성화

- VSCode에서 설정

1. Prettier 확장 설치
2. settings에 추가 
```json
{
  "javascript.format.enable": false,
  "typescript.format.enable": false
}
```