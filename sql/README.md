# ORACLE SQL

## GROUP BY
* TO_CHAR(): 날짜 및 시간 변환 함수
```
TO_CHAR(SYSDATE,'YYYYMMDD') -- 20200123
TO_CHAR(SYSDATE,'HH24') -- 시간을 0~23시 형식으로 표현
```
* LEVEL과 CONNECT BY
```
SELECT LEVEL FROM dual CONNECT BY LEVEL <=5; -- 12345가 있는 Level 속성 테이블
```
* NVL
```
NVL(COUNT, 0) -- COUNT가 NULL이면 0
```
* OUTER JOIN
```
FROM A, B
WHERE A.COL = B.COL(+) -- LEFT OUTER JOIN
```
  * 매칭되는 데이터가 없으면 NULL