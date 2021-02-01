import sys
# 유니온 파인트
n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n+1)] # parent[i]: i 노드의 부모 노드

def find(x):
    if parent[x] == x:
        return x;
    else:
        y = find(parent[x])
        parent[x] = y
        return y

def union(x, y):
    x = find(x)
    y = find(y)
    if (x != y):
        parent[y] = x

while True:
    try:
        op, a, b = map(int, sys.stdin.readline().split())
    except:
        break
    if op == 0:
        union(a, b)
    else:
        aParent = find(a)
        bParent = find(b)
        if aParent == bParent:
            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")
