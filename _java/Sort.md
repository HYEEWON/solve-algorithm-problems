# 정렬

## Arrays.sort(array)
* 배열 정렬 ex) int[], double[], char[], Object[] 등
```java
String[] s = {"d", "a", "e", "b", "c"};

Arrays.sort(s);
System.out.println(Arrays.toString(s)); // [a, b, c, d, e]

Arrays.sort(s, Comparator.reverseOrder());
System.out.println(Arrays.toString(s)); // [e, d, c, b, a]

Arrays.sort(s, 2, 4); // index 2~3을 정렬
System.out.println(Arrays.toString(s)); // [e, d, b, c, a]
```
## Collections.sort(list)
* List Collection 정렬 ex) ArrayList, Vector 등
```java
List<Integer> list = new ArrayList<>();
list.add(3);
list.add(1);
list.add(2)

Collections.sort(list);
System.out.println(list); // [1, 2, 3]

Collections.sort(list, Collections.reverseOrder());
System.out.println(list); // [3, 2, 1]
```

## Comparable & Comparator 인터페이스
* Primitive형은 적용 불가능, Wrapper Class 가능
### Comparator -> compare()
* 1차원 배열
```java
Arrays.sort(array, new Comparator<Integer>(){ 
    @Override
    public int compare(Integer i1, Integer i2) { // 올림차순
        if (i1 > i2) return 1;
        else if (i1 < i2) return -1;
        else return 0;
    }
});
```
* 2차원 배열
```java
Arrays.sort(array, new Comparator<Integer[]>(){ 
    @Override
    public int compare(Integer[] i1, Integer[] i2) { // 올림차순
        if (i1[0] > i2[0]) return 1;
        else if (i1[0] < i2[0]) return -1;
        else return 0;
    }
});
```
```java
Arrays.sort(array, new Comparator<Integer[]>(){
    @Override
    public int compare(Integer[] i1, Integer[] i2) {
        if (i1[0] > i2[0]) return 1; // 올림차순
        else if (i1[0] == i2[0]) {
            if (i1[1] > i2[1]) return 1; // 올림차순
        }
        return -1;
    }
});
```
* 양수인 경우에는 위치 교환, 음수 또는 0인 경우는 자리 유지
### Comparable -> compareTo()
```java
class Point implements Comparable<Point> {
    int x, y;

    @Override
    public int compareTo(Point p) {
        if(this.x > p.x) {
            return 1; // x에 대해서는 오름차순
        }
        else if(this.x == p.x) {
            if(this.y < p.y) { // y에 대해서는 내림차순
                return 1;
            }
        }
        return -1;
    }
}
```