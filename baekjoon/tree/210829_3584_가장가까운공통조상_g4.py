import sys
from collections import defaultdict
sys.setrecursionlimit(100000)

def dfs(now, depth):
    visit[now] = True
    depths[now] = depth

    for node in tree[now]:
        if visit[node]:
            continue
        parents[node][0] = now
        dfs(node, depth+1)

def dp():
    global max_depth
    for i in range(1, max_depth):
        for j in range(1, N+1):
            parents[j][i] = parents[parents[j][i-1]][i-1]

def lca(a, b):
    if depths[a] > depths[b]:
        a, b = b, a

    for depth in range(max_depth-1, -1, -1):
        if depths[parents[b][depth]] >= depths[a]:
            b = parents[b][depth]

    if a == b:
        return a

    for depth in range(max_depth-1, -1, -1):
        if parents[a][depth] != parents[b][depth]:
            a = parents[a][depth]
            b = parents[b][depth]

    return parents[a][0]


T = int(sys.stdin.readline())

for t in range(T):
    N = int(sys.stdin.readline())
    tree = defaultdict(list)
    roots = [True for i in range(N+1)]

    for n in range(N-1):
        # a가 b의 부모
        a, b = map(int, sys.stdin.readline().strip().split())
        tree[a].append(b)
        tree[b].append(a)
        roots[b] = False

    a, b = map(int, sys.stdin.readline().strip().split())

    tmp = 1;
    max_depth = 0;
    while tmp <= N:
        tmp <<= 1
        max_depth += 1

    visit = [False for i in range(N+1)]
    depths = [0 for i in range(N+1)]
    parents = [[0 for i in range(max_depth)] for j in range(N+1)]

    root = roots[1:].index(True) + 1
    dfs(root, 1)
    dp()

    sys.stdout.write(str(lca(a, b)) + "\n")