import sys

a_cnt, b_cnt = map(int, sys.stdin.readline().split())
A = set(map(int, sys.stdin.readline().strip().split()))
B = set(map(int, sys.stdin.readline().strip().split()))

## 첫 번째 풀이
sys.stdout.write(str(len(A-B) + len(B-A)))

## 두 번째 풀이
A_intersection_B = A.intersection(B)
sys.stdout.write(str(a_cnt+b_cnt-2*len(A_intersection_B)))