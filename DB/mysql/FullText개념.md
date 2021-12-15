# FULLTEXT 개념

- 일반적인 Mysql 검색은 % (like)으로 이루어집니다.

- 하지만 like 검색은 FULLINDEX로 처음부터 끝까지 검색하기 때문에 데이터가 많아지면 속도가 현저히 떨어집니다.

- Mysql5.7부터 InnoDB와 MyISAM테이블에서 추가된 Full-Text검색과 N-그램 방식으로 전문적인 검색 엔진을 사용할 수 있게 되었습니다.

- FULLTEXT 이름대로 index를 FULLTEXT로 저장하게 되면 지정된 구분자대로 따로 저장하게 되고 검색했을 때 빠르게 찾을 수 있게 됩니다.

