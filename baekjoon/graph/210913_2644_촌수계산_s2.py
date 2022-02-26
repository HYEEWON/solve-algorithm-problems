import sys
from collections import defaultdict

answer = -1

def dfs(a, b, cnt):
    global answer

    if a == b:
        answer = cnt
        return

    for p in relations[a]:
        if visit[p]:
            continue

        visit[p] = 1
        dfs(p, b, cnt + 1)

N = int(sys.stdin.readline())
x, y = map(int, sys.stdin.readline().strip().split())

M = int(sys.stdin.readline())
relations = defaultdict(list)
for m in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    relations[a].append(b)
    relations[b].append(a)

visit = [0 for i in range(N + 1)]
visit[x] = 1
dfs(x, y, 0)

sys.stdout.write(str(answer))