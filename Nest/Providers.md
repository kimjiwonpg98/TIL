# Providers

- 종속성을 주입하는 중요한 기능 중 하나!
- 객체는 서로 다양한 관계를 만들 수 있으며 객체의 인스터스를 연결하는 기능

필요한 준비물: Services, Modules

## Example
----

### **cats.service.ts** (데이터 저장 및 검색 담당) => Controller에서 사용
```js
import { Injectable } from '@nestjs/common';
import { Cat } from './interfaces/cat.interface';

@Injectable()
export class CatsService {
  private readonly cats: Cat[] = [];

  create(cat: Cat) {
    this.cats.push(cat);
  }

  findAll(): Cat[] {
    return this.cats;
  }
}

```

### **cat.interface.ts**

```js
export interface Cat {
  name: string;
  age: number;
  breed: string;
}
```

### **cat.controller.ts**

```js
import { Controller, Get, Post, Body } from '@nestjs/common';
import { CreateCatDto } from './dto/create-cat.dto';
import { CatsService } from './cats.service';
import { Cat } from './interfaces/cat.interface';

@Controller('cats')
export class CatsController {
  constructor(private catsService: CatsService) {}

  @Post()
  async create(@Body() createCatDto: CreateCatDto) {
    this.catsService.create(createCatDto);
  }

  @Get()
  async findAll(): Promise<Cat[]> {
    return this.catsService.findAll();
  }
}
```

- CatsService를 private로 받아오면서 종속성을 주입
- constructor에서 this로 초기화시켜주지 않아도 되는 이유는 module때문


### **app.module.ts**
```js
app.module.tsJS

import { Module } from '@nestjs/common';
import { CatsController } from './cats/cats.controller';
import { CatsService } from './cats/cats.service';

@Module({
  controllers: [CatsController],
  providers: [CatsService],
})
export class AppModule {}
```
- providers에 CatsService를 넣어줌으로써 서비스를 등록


----

쉬운 설명

- Controller: 소비자
- Service: 제품을 제공


---

## 참고 문헌
- [공식홈페이지](https://docs.nestjs.com/providers)

