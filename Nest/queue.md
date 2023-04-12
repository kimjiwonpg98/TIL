## NESTJS에서의 큐 사용기

### 사용 스택

- 프레임워크: NestJS
- 언어: typescript
- 저장소: Redis

### 사용하는 이유

사실 큐를 사용하는 것에는 여러가지 경우가 있을 것입니다. </br>
트래픽이 몰리거나 문제가 생겼을 때 어디에 안전하게 저장한 후 재처리하기 위한 경우도 있을 것이고 동시성 문제를 해결하기 위해 사용하는 경우도 있을 것입니다.</br>
필자는 그 중에서도 비동기적으로 수행하기 위해 큐를 사용하게 되었습니다.(사용량 체크)

### 간단한 개념 설명

우리가 알아야할 것은 딱 3가지입니다.

1. Producer (생산자)
2. Queue (임시 저장소)
3. Consumer (처리자)

이렇게 3가지의 주체가 메시지 큐를 운영하게 됩니다. 그 과정을 간단하게 요약하면 아래와 같습니다.

1. Producer가 할 일을 정의한 메시지를 Queue에 저장
2. Consumer가 Queue에서 메시지를 가져와서 작업을 수행

사실상 카프카의 심플 버전이라고 봐도 될 것 같습니다.

### 기본 설치

[NestJS 공식 홈페이지](https://docs.nestjs.com/techniques/queues)에 나와있는대로 bull 패키지를 설치해줍니다.

```
npm install --save @nestjs/bull bull
```

### 기본 세팅

#### 1. 모듈 추가

필자는 **configService**를 이용해 환경변수에서 redis의 설정값을 가져올 것이기 때문에 factory함수를 사용할 수 있는 **forRootAsync**를 사용하여 모듈을 추가해주었습니다.

- app.module.ts

```ts
import { Module } from '@nestjs/common';
import { BullModule } from '@nestjs/bull';
import { ConfigModule, ConfigService } from '@nestjs/config';
import { queueFactory } from './config/queue.config';

@Module({
  import: [
    ConfigModule.forRoot({ isGlobal: true }),
    BullModule.forRootAsync({
      imports: [ConfigModule],
      useFactory: queueFactory,
      inject: [ConfigService],
    })
  ]
})
```

- queue.config.ts

```ts
import { ConfigService } from '@nestjs/config';
import { EnvVars } from './env.validation';

export const queueFactory = (configService: ConfigService<EnvVars, true>) => ({
  redis: {
    host: configService.get<string>('REDIS_HOST', { infer: true }),
    port: configService.get<number>('REDIS_PORT', { infer: true }),
    db: configService.get<number>('REDIS_DB', { infer: true }),
  },
});
```

Bull를 사용할 레디스를 종속시켜줬으니 이제 큐를 등록해봅시다.

자신이 큐를 사용할 모듈에서 registerQueue를 사용해 등록해줍니다.
저는 글로벌 인터셉터에서 사용할 것이기 때문에 app.module 에서 등록해주었습니다.

```ts
BullModule.registerQueue({
  name: 'use-check',
});
```

name으로 이름을 등록하여 producer가 알 수 있도록 해줍니다.
그럼 이렇게 레디스에 등록이 된 것을 볼 수 있습니다.
![9D5AAC61-94FA-4C81-AD32-45561EB6ED47](https://user-images.githubusercontent.com/75289370/231488781-1f621ba7-4315-4532-b892-b0015e051c64.jpeg)

### 실행 방법

- use-check라는 큐까지 등록을 했으니 큐에 메시지를 저장할 producer를 만들어줘야합니다.
- producer는 어디서든 어디든 상관없습니다 종속성 주입이 가능한 곳(@Injectable()이 있는 곳)에서 생성자 안에 주입해주면 됩니다.

백문이 불여일견 코드로 알아봅시다.
필자는 인터셉터에 넣었으니 인터셉터를 예시 코드로 보여드리겠습니다.

#### Producer

```ts
import { InjectQueue } from '@nestjs/bull';
import { Queue } from 'bull'; // 나머지 import는 생략

@Injectable()
export class ClientInterceptor implements NestInterceptor {
  private readonly redisClient: Redis;
  constructor(
    @InjectQueue('use-check')
    private useCheckQueue: Queue, // @InjectQueue('등록한 큐 이름') 을 이용해 종송성 주입
    private reflector: Reflector,
    private readonly redisService: RedisService,
  ) {
    this.redisClient = redisService.getClient();
  }

  public async intercept(
    context: ExecutionContext,
    next: CallHandler,
  ): Promise<Observable<any>> {
    return next.handle().pipe(
      catchError(async (err) => {
        if (await this.redisClient.get('stop')) {
          await this.useCheckQueue.pause(); // consumer 처리 정지
        } else {
          await this.useCheckQueue.resume(); // consumer 처리 다시 시작
        }

        await this.useCheckQueue.add(
          // 큐에 저장
          'use',
          `${req.method}>${req.route.path}>fail`,
          { removeOnComplete: true }, // 작업 저장 성공 시 redis 데이터 삭제
        );
        throw err;
      }),
      tap(async (n) => {
        if (await this.redisClient.get('stop')) {
          await this.useCheckQueue.pause();
        } else {
          await this.useCheckQueue.resume();
        }

        await this.useCheckQueue.add(
          'use',
          `${req.method}>${req.route.path}>>success`,
          { removeOnComplete: true },
        );
        return n;
      }),
    );
  }
}
```

add 메서드가 실행되면</br>
첫번째 인자로 넣은 값을 key로 하는 작업이 하나 추가되고</br>
두번째 인자로 들어가있는 내용이 레디스의 value로 들어갑니다.
```
!!! 주의할 점
두번쨰 인자의 값에 따라 레디스의 타입이 지정되니 저장 후 한번씩 확인이 필요합니다.
```

그리고 메서드에는 여러가지의 옵션값이 있는데 필자는 레디스에 작업이 남는게 싫어서 **removeOnComplete** 옵션을 켜두었습니다.

기존처럼 내비두면 작업이 hash 타입으로 저장되게 되고 아래 사진처럼 저장되게 됩니다.
![CB01BDE5-8FF9-4BCB-B1EC-3634802FAA66_1_201_a](https://user-images.githubusercontent.com/75289370/231488831-1d85b292-01b1-46df-86f9-3fbbac423d07.jpeg)

마지막으로 저는 사용량 체크이기 떄문에 값을 업데이트할 때는 간단한 lock(레디스에 key 추가)과 **pause와 resume** 메서드를 이용해</br>
consumer가 큐에서 작업을 꺼내오지 못하도록 조절해주었습니다.

- pause: consumer 처리 일시 정지
- resume: consumer 처리 재시작

#### Consumer

- 마지막으로 producer가 큐에 넣은 작업을 실행하는 consumer를 보겠습니다.

```ts
import { Process, Processor } from '@nestjs/bull';
import { Job } from 'bull';
import { RedisService } from '@liaoliaots/nestjs-redis';
import Redis from 'ioredis';

@Processor('use-check') // 등록한 큐를 보는 데코레이터
export class UseCheckProcessor {
  private readonly redisClient: Redis;
  constructor(private readonly redisService: RedisService) {
    this.redisClient = redisService.getClient();
  }

  @Process('use')   // use 작업을 진행
  async transcode(job: Job<string>) {
    // job.data로 작업 진행
  }
}
```

- @Processor('큐 이름') 작업 핸들러를 선언 후 큐에 처리하는 작업이 있을 때마다 호출됩니다.
- 그리고 @Process('특정 작업 이름') 에서 특정 작업만 처리하도록 지정하여 작업을 실행했습니다.
- 아무것도 넣지 않는다면 모든 작업을 처리하도록 할 수 있습니다.


- job.data에는 위에서 저장해둔 두번째 인자에 들어간 value값이 들어가 있습니다.
- 사용자는 입맛에 맞게 그 값을 실행하면 됩니다.



### 사용 후기

필자는 정말 만족하며 사용하고 있고 간단한 큐나 동시성 이슈가 있는 작업에서 사용하면 알맞게 사용할 수 있어 nestJS를 사용하며 애용할 것입니다.
job options 에는 더 많은 옵션값들이 있고 우선순위, delay 등 여러 옵션을 더 사용해보고 나중에 더 좋은 글을 써보겠습니다!


### 도움이 된 곳
- [NESTJS 공식 홈페이지](https://docs.nestjs.com/techniques/queues)
- [블로그](https://overcome-the-limits.tistory.com/679?category=1006727)
- 
