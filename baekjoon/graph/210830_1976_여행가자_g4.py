# 유니온 파인드

import sys
from collections import defaultdict

def find(x):
    if parents[x] == x:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parents[y] = x

N = int(sys.stdin.readline()) # 노드 수
M = int(sys.stdin.readline())
graph = defaultdict(list)
parents = [i for i in range(N+1)]

for n in range(1, N+1):
    link = list(map(int, sys.stdin.readline().strip().split()))
    for i in range(N):
        if link[i] == 1:
            union(n, i+1)

path = list(map(int, sys.stdin.readline().strip().split()))

tmp = find(path[0])
flag = True
for p in path:
    if tmp != find(p):
        flag = False
        break

if flag:
    sys.stdout.write("YES\n")
else:
    sys.stdout.write("NO\n")
