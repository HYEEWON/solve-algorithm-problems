# 정규식 표현

## 패키지 추가
```python
import re
```
## 문자 클래스: []
* `[] 사이의 문자들과 매칭`
* `\d` - 숫자와 매치, `[0-9]`와 동일
* `\D` - 숫자가 아닌 것과 매치, `[^0-9]`와 동일
* `\s` - whitespace 문자와 매치, `[ \t\n\r\f\v]`와 동일(맨 앞의 빈 칸은 * `공백`문자(space)를 의미)
* `\S` - whitespace 문자가 아닌 것과 매치, `[^ \t\n\r\f\v]`와 동일
* `\w` - 문자+숫자와 매치, `[a-zA-Z0-9_]`와 동일
* `\W` - 문자+숫자가 아닌 문자와 매치, `[^a-zA-Z0-9_]`와 동일

## Dot: .
* `\n을 제외한 모든 문자`와 매치(최소 1개 이상의 문자 필수)
* `a.b`: a + 문자 + b
* `a..b`: a + 문자 + 문자 + b

## 반복
* `*`: 문자의 `0번 이상` 반복
* `+`: 문자의 `1번 이상` 반복
* `{m,n}`: `m~n번` 반복
  * {1,}은 +와 동일하고, {0,}은 *과 동일
  * `ab{2}c`: abbc
* `?`: `{0, 1}`

## 예시
* findall
  * 결과를 `list`로 반환
    ```python
    text = "This is String!!"
    
    print(re.findall(r'[\s\S]+',text)) # ['This is String!!']
    print(re.findall(r'[\S]+',text)) # ['This', 'is', 'String!!']
    print(re.findall(r'[a-zA-Z]+',text)) # ['This', 'is', 'String']
    ```
* match
  * 문자열의 처음부터 일치하는 부분을 찾음(없으면 None 반환)
  * 문자열의 시작 부분부터 일치해야 함
  ```python
  text = 'izizi'
  print(re.match('ziz', text)) # None
  print(re.match('izi', text)) # <_sre.SRE_Match object; span=(0, 3), match='izi'>
  print(re.match('izi', text).group()) # izi
  ```
* search
  * 문자열의 처음부터 일치하는 부분을 찾음(없으면 None 반환)
  * 문자열의 시작 부분부터 일치하지 않아도 됨
  * 매칭이 한 번 되면 검사 중지
  ```python
  text = 'izizi'
  print(re.search('ziz', text).group()) # ziz
  print(re.search('izi', text).group()) # izi
  ```
```python
m = re.search('\d{4}-(\d?\d)-(\d?\d)', '1868-12-10')
print(m.group()) # 1868-12-10
print(m.group(0)) # 1868-12-10
print(m.group(1)) # 12
print(m.group(2)) # 10
print(m.groups()) # ('12', '10')
```
* group
  * 매치된 문자열 반환
* groups
  * `()`으로 캡처한 부분
* start
  * 매치된 문자열의 시작 인덱스
* end
  * 매치된 문자열의 끝 인덱스