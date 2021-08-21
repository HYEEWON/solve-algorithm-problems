# 그리디(탐욕) 알고리즘

* 현재 상황에서 지금 당장 좋은 것만 고르는 방법
* 단순히 최선의 선택을 반복해도 최적 해를 구할 수 있는지 검토 필요

## (문제) 거스름 돈
500, 100, 50, 10원의 동전을 사용해 N원을 거슬러 줄 때, 사용할 동전의 최소 개수는? (N은 10의 배수)
* 가장 큰 화폐 단위부터 돈을 거슬러 줌
* 큰 단위가 항상 작은 단위의 `배수`이기 때문에 최적 해 보장 가능
```python
n = 1260
count = 0
money = [500, 100, 50, 10]
for m in money:
    count += (n//m)
    n %= coin
print(count)
```
```java
public class Main{
    public static void main(String[] args) {
        int n = 1260;
        int count = 0;
        int[] money = {500, 100, 50, 10};
        for (int m : money) {
            count += (n/m);
            n %= m;
        }
        System.out.println(count);
    }
}
```