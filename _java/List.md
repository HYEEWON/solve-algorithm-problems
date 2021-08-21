# 배열
## 1차원 배열
```java
int[] arr = new int[5]; // [0, 0, 0, 0, 0] 
System.out.println(arr.length); // 5
arr[0] = 5; // [5, 0, 0, 0, 0] 
System.out.println(arr); // 불가능
```
  * 자동으로 0으로 초기화(실수: 0.0, 객체: null)
```java
int[] arr1 = new int[5] {1, 2, 3, 4, 5}; // 오류 
int[] arr2 = new int[] {1, 2, 3, 4, 5}; // 가능
int[] arr3 = {1, 2, 3, 4, 5}; // 가능
int[] arr4;
arr4 = new int[] {1, 2, 3, 4, 5} // 가능
```
## 다차원 배열
```java
int[][] arr1 = new int[2][3]; // 행: 2, 열: 3
int[][] arr2 = {{1, 2, 3}, {4, 5, 6}};
```

# ArrayList
* 동적 크기 변경 가능
* 클래스
```java
ArrayList<E> list = new ArrayList<>();
System.out.println(list.size()); // 0
list.add(value); // 값
list.add(idx, value) // index에 값 추가
list.remove(idx); // index
System.out.println(list); // 가능
```

# List
* 인터페이스

# Arrays
```java
String[] s = {"d", "a", "C", "b", "c"};
System.out.println(Arrays.toString(s)); //배열의 모든 원소를 문자열로 바꾸어 반환
```