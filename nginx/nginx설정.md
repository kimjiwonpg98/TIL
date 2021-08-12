# nginx 설정

## nginx 설치

```
sudo apt-get install nginx (ubuntu 기준)
```

- 확인 방법: nginx -v
- 기동 방법: nginx
- 정지 방법: nginx -s stop
- 재가동 방법: nginx -s reload

## nginx.conf

- nginx의 설정이 들어가는 핵심 파일

```
worker_processes  1;
events {
    worker_connections  1024;
}
http { 
    include       mime.types;
    server {
        listen       80;
        location / {
            root   html;
            index  index.html index.ht m;
        }
    }
}
```
- worker_processes: core 모듈 설정
  - 몇 개의 워커 프로세스를 생성할 것인지 지정하는 지시어    
  🕵️‍♀️ 1이면 하나의 코어만으로 요청을 처리한다는 뜻

- events: 네트워크 동작방법과 관련된 설정
  - worker_connections: 하나의 프로세스가 처리할 수 있는 커넥션의 수    
  ✨ 최대 접속자 수 = worker_processes * worker_connections

- http 블록: server 블록, location블록의 루트 블록
  - 관리상 이슈로 한번만 사용하는 것을 권장합니다.

- server 블록: 하나의 웹사이트를 선언하는데 사용    
  🕵️‍♀️ 여러 server 블록을 사용하면 한대의 머신에 여러 웹사이트를 서빙할 수 있습니다.    
  ✨ 즉 호스트는 한 개지만 가상으로 호스트가 여러 개인 것처럼 동작합니다.    
  - 이것을 **가상 호스트**라고 합니다.
  - listen: 웹사이트가 바라보는 포트를 의미합니다.

- location 블록: server의 하위 블록으로 특정 웹사이트의 url를 처리하는데 사용    


- nginx는 무중단배포도 가능하고 로드밸런싱 기술도 따라할 수 있는 강력한 웹서버입니다.
- 다른 여러 설정은 다시 정리하도록 하겠습니다.




-----

- [참고 블로그](https://juneyr.dev/nginx-basics)