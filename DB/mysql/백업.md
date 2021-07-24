# 📖 데이터 백업

데이터 백업은 데이터베이스 관리에서 가장 중요한 작업 중에 하나로 뽑힙니다.

## 참고
데이터가 유실될 경우 백업 DB를 검사하여 해당 날짜와 원하는 데이터를 백없할 수 있도록 설정해두어야 합니다.


## 📄 전체 백업
-------
<br>

### 🐱‍🏍 실행 순서

1. sudo su
2. 백업 자료가 저장될 폴더를 만듭니다. => mkdir /backup
3. chmod 755 backup
4. nano /root/backup.sh
```
DATE=`/bin/date +"%Y%m%d"` 
PREV_DATE=`/bin/date --date '5 days ago' +"%Y%m%d"`
/usr/bin/mysqldump -u사용자id -p사용자pw DB명 > /backup/mysql_backup_${DATE}.sql
chown root.root  /backup/mysql_backup_${DATE}.sql
chmod 755  /backup/mysql_backup_${DATE}.sql
rm -Rf  /backup/mysql_backup_${PREV_DATE}.sql
```
✨ 5일되면 자동 삭제 되도록 합니다.

5. chmod 100 /root/backup.sh  변경방지위해 실행권한만 줍니다.

6. test => /root/backup.sh

### crontab에 작업 등록
1. crontab -e  크론 탭 작성모드로 실행합니다.
2. crontab안에 00 04 * * * /root/backup.sh
> 작업 스케줄의 시간은 min(분) hour(시간) day(일) month(달) weekday(요일) 한 칸씩 띄워서 적어줍니다. 그다음 실행할 파일을 적어주시면 됩니다.
     
3. service cron restart 크론 데몬 재실행
✨ crontab -l 작업 리스트 확인 


💫 전체 백업 시 mysql -u  [db id명] -p < backupfile.sql

<br>


## 📄 부분 백업
---------
### 🐱‍🏍 부분log 설정법
<br>

1. nano /etc/mysql/my.cnf 이동
2. 명령어 입력
```
server-id= 숫자 #mysql서버 id
user= ~~ #mysql 유저이름
log-bin= #binlog 파일명
binlog_cache_size = 2M #캐시사이즈
max_binlog_size = 256M #로그 최대 사이즈
expire_logs_days = 3 #보관 기간
binlog_format = 2 #binlog 포맷(ROW)
```
3. mysql에서 설정
    - set global expire_logs_days=3;
    - show variables like '%expire%';

### 부분 log  사용법
1. /var/lib/mysql 폴더로 이동
2. **명령어** mysqlbinlog --no-defaults -v marialog.000001 > binlog/show.log
3. binlog 폴더로 이동 후 vi show.log로 백업할 시간이나 아이디를 보고 다시 로그 만듭니다.
4. 실행방법

> ``mysqlbinlog --no-defaults --start-datetime="2021-05-25 15:55:55" --stop-datetime="2021-05-25 20:20:20" -d [db명] marialog.000013 > binlog/fix.log`` 
 
> ``mysqlbinlog --no-defaults --start-position="123456" --stop-position="3445530" -d [db명] marialog.000013 > binlog/fix.log``

5. mysql -u [db id명] -p < fix.log





## 참고 자료
> [전체 백업](https://code-aid.tistory.com/7)
> [백업참고동영상](https://www.youtube.com/watch?v=7_cilpkXfAA&t=778s)
> [부분 백업](https://93it-security-service.tistory.com/38)