import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())
graph = defaultdict(list)

for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visit = [0] * (N+1)
answer = 0

def dfs(x):
    for node in graph[x]:
        if visit[node] == 0:
            visit[node] = 1
            dfs(node)

for i in range(1, N+1):
    if visit[i] == 0:
        answer += 1
        visit[i] = 1
        dfs(i)

sys.stdout.write(str(answer))