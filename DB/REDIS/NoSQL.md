# NoSQL (Not Only SQL)

## 개념
- 관계형 모델을 사용하지 않고 테이블 간에 조인 기능 X
- 비관계적인 데이터 저장소이며 비구조적인 데이터를 저장하기 위한 **분산 저장 시스템**
- 데이터 저장 및 검색에 특화되어 있습니다.

## 등장 이유
> SQL 서버의 확장성에 이유가 있습니다.   

- 트래픽이 늘어서 CPU 혹은 메모리의 사용량이 늘어나 서비스가 비정상화될 때 계속 스케일 업을 하는 것에는 한계점이 분명합니다.

🔗 MYSQL 테스트 자료에 따르면 CPU 16코어를 넘어가면 성능 증가가 미미하다고 합니다.

- 반면에 NoSQL은 처음부터 스케일 아웃을 염두로 설계했기 때문에 새로운 하드웨어를 추가하면 그만입니다.


## NoSQL을 사용하기 좋은 상황
- 데이터 증가량이 측정하기 불가능하거나 서비스 요청량의 증가를 예측하기 어려운 상황