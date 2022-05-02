## 1. 개요 🤸‍♂️
<br>


서버 쪽 코드를 관리할 때 항상 사용하는 것이 하나 있습니다.
그것은 환경설정할 때 필요한 환경 변수들이다. Node 기준으로 .env 파일에서 관리를 하게 되는데
이것도 환경별로 나누어 사용할 경우가 있습니다.

이번에는 nest에서 사용하는 .env파일 사용법에 대해 정리해보려고 합니다.


## 2. 🤔 왜 @nestjs/config로?
<br>

기본적으로 express를 이용해 환경변수를 사용할 때는 dotenv 모듈을 이용해 관리했었다.

ex)
```js
import * as dotenv from 'dotenv';

const PORT = process.env('PORT');
```

하지만 [nestjs 공식문서](https://docs.nestjs.com/techniques/configuration#custom-env-file-path)에서는 **@nestjs/config** 모듈을 사용한다.

> 사실 @nestjs/config 내부적으로는 dotenv를 사용하고 있어서 그대로 해도 되긴하지만 nestjs에 맞춰 나온 모듈이기 때문에 사용하는 것이 좋습니다.


## 3. 👨‍💻 설정 방법

<br>

환경에 맞춰 .env파일도 다르게 구성해야된다.
product같은 경우는 클라우드 단에서 설정하면 되기 때문에 .env 파일을 따로 구성해주지않았다.

파일은 그래서 `.dev.env`, `.local.env`로 구성하였다.


**app.module**

```ts
import { ConfigModule } from '@nestjs/config';
...


@Module({
  imports: [
    ConfigModule.forRoot({
      isGlobal: true, // 전체적으로 사용하기 위해
      envFilePath: `.${process.env.NODE_ENV}.env`,
    })
  ]
  ...
})

```

이런 식으로 구성한 후 NODE_ENV를 사용해주기 위해 [cross-env](https://www.npmjs.com/package/cross-env)모듈을 하나 더 설치


package.json

```json
"script": {
    "start:local": "cross-env NODE_ENV=local nest start --watch",
  	"start:devops": "cross-env NODE_ENV=dev nest start --watch",

}
```
이렇게 NODE_ENV를 적어주면 설정은 끝..!



## 4. 👨‍💻 사용 방법
<br>


사용하는 방법은 여러가지다.

원래 사용방법처럼 **process.env.name** 이런 식으로 사용할 수 있습니다.

하지만 isGlobal을 사용하지 않을 경우 사용하는 주체에서 **ConfigService**를 import 해야한다.


**User.Service.ts**
```ts
import { ConfigService } from '@nestjs/config';

@Injectable()
export class UserService {
 constructor (private readonly config: ConfigService) {}
  
 private domain = this.config.get<string>('GATEWAY_DOMAIN', 'localhost');
 ...
}
```
첫번째 인자에 환경변수 키값을 넣어준다. 그리고 두 번째 인자에 기본값을 넣어줄수도 있다. (undefined일 때)
필자는 nest의 방식인 configservice를 가져오는 방식으로 사용하고 있다.


## 5. 유효성 검사하기
<br>

환경 변수가 잘못 들어가거나 본인이 원하지않는 값으로 들어가는 경우도 있어

`class-validator`와 `class-transformer`를 사용하여 커스텀하여 유효성 검사 실행


**env.validation.ts**

```ts
import { plainToClass } from 'class-transformer';
import { IsEnum, IsNumber, validateSync } from 'class-validator';

enum Environment {
  Local = "local",
  Dev = "dev",
}

class EnvironmentVariables {
  @IsEnum(Environment)
  NODE_ENV: Environment;

  @IsNumber()
  PORT: number;
}

export function validate(config: Record<string, unknown>) {
  const validatedConfig = plainToClass(
    EnvironmentVariables,
    config,
    { enableImplicitConversion: true },
  );
  const errors = validateSync(validatedConfig, { skipMissingProperties: false });

  if (errors.length > 0) {
    throw new Error(errors.toString());
  }
  return validatedConfig;
}
```

**app.module.ts**

```ts
import { ConfigModule } from '@nestjs/config';
import { validate } from 'src/util/validate/env.validation';
...


@Module({
  imports: [
    ConfigModule.forRoot({
      envFilePath: `.${process.env.NODE_ENV}.env`,
      validate
    })
  ]
  ...
})

```