# Controller

- 들어오는 요청을 처리하고 응답을 반환해주는 파트

- 애플리케이션에 대한 특정 요청을 수신

<br>
<br>


## 👷‍♂️ 컨트롤러를 만드는 방법
------
  ⭐ 준비물: 클래스와 데코레이터(@)

1. 데코레이터로 클래스를 **필수 메타데이터**와 연결
2. Nest가 라우팅 맵(라우팅 경로)을 만들 수 있도록 한다.

> 😁 꿀팁 <br>
 validation이 내장된 CRUD 컨트롤러를 만들때는 **nest g 이름**으로 빠르게 만들 수 있다! <br>
 컨트롤러만 만드려면 **nest g controller 이름**
## 컨트롤러 사용하는 방법

- @Controller(): 기본 컨트롤러를 정의하는 데코레이터

```js
//example.controller.ts

import { Controller, Get, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("route")  // 1
export class ExampleController {
  @Get()   // 2
  findAll(@Req() request: Request): string {   // 3
    return "This is example";
  }
}

```

1. 이렇게 Controller의 Decorator에 class 전체의 경로를 적어주면 GET /route 경로에 요청을 매핑하게 된다.
2. Get Decorator에 경로를 적게 되면 각자의 경로가 만들어진다 **ex) GET /route/example**
3. Req Decorator을 이용해 요청객체에 대한 액세스를 제공하기도 한다. (Req, Res, Next)
  - 필자는 express을 플랫폼으로 하였다. (express, @types/express 패키지 설치 필수!)


## 📃 상태 코드
--------------------------------

⭐ 상태코드는 POST의 201을 제외하고는 기본적으로 200이 반환된다!

- HttpCode Decorator을 이용해 다른 상태코드를 반환시킬 수 있다.
```js
@Post()
@HttpCode(204)
create() {
  return "statuscode changed";
}
```


## 🔗 Headers
-----

상태코드와 같이 HttpMethod Decorator아래에 @Header Decorator를 해준 후 적어주면 된다.