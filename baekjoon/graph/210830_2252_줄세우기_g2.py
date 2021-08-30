# 위상 정렬

import sys
from collections import defaultdict, deque

N, M = map(int, sys.stdin.readline().strip().split())

indegree = [0 for i in range(N+1)]
graph = defaultdict(list)
q = deque()

for m in range(M):
    # A가 B보다 앞에 있어야 함
    A, B = map(int, sys.stdin.readline().strip().split())
    indegree[B] += 1
    graph[A].append(B)

for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)


while q:
    front = q.popleft()
    sys.stdout.write(str(front) + " ")
    for idx in graph[front]:
        indegree[idx] -= 1
        if indegree[idx] == 0:
            q.append(idx)