# 정규식 표현

## 문자 클래스: []
* `[] 사이의 문자들과 매칭`
* `\d` - 숫자와 매치, `[0-9]`와 동일
* `\D` - 숫자가 아닌 것과 매치, `[^0-9]`와 동일
* `\s` - whitespace 문자와 매치, `[ \t\n\r\f\v]`와 동일(맨 앞의 빈 칸은 * `공백`문자(space)를 의미)
* `\S` - whitespace 문자가 아닌 것과 매치, `[^ \t\n\r\f\v]`와 동일
* `\w` - 문자+숫자와 매치, `[a-zA-Z0-9_]`와 동일
* `\W` - 문자+숫자가 아닌 문자와 매치, `[^a-zA-Z0-9_]`와 동일
* `\b` - 공백을 찾음

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

## String 메소드
* String.matches()
* String.split()
* String.replaceFirst()
* String.replaceAll()
```java
String text = "This is String!!";
String pattern = "[\\s\\S]+";
System.out.println(text.matches(pattern)); // true

pattern = "\\s";
System.out.println(Arrays.asList(text.split(pattern) // [This, is, String!!]

pattern = "Hello";
System.out.println("Hello World Hello World ".replaceFirst(patte"Regex")); // Regex World Hello World
System.out.println("Hello World Hello World ".replaceAll(patte"Regex")); // Regex World Regex World
```


## 클래스: Pattern, Matcher
```java
import java.util.regex.Pattern;
import java.util.regex.Pattern;

Pattern pattern = Pattern.compile("\\bcat\\b");
Matcher matcher = pattern.matcher("cat cat cat cattie cat");
int count = 0;
while(matcher.find()) {
    count++;
    System.out.println("Match number " + count);
    System.out.println("group(): " + matcher.group());
    System.out.println("start(): " + matcher.start());
    System.out.println("end(): " + matcher.end());
}
```
```
Match number 1
group(): cat
start(): 0
end(): 3
Match number 2
group(): cat
start(): 4
end(): 7
Match number 3
group(): cat
start(): 8
end(): 11
Match number 4
group(): cat
start(): 19
end(): 22
```