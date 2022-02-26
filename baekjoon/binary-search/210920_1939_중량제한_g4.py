## 이분탐색
## 가능한 weight를 이분탐색으로 찾고 -> 이동이 가능하면 정답

import sys
from collections import defaultdict
sys.setrecursionlimit(10**5)

class Node:
    def __init__(self, node, weight):
        self.node = node;
        self.weight = weight;

def dfs(node, weight):
    global T2, isConnect

    visit[node] = True
    if node == T2:
        isConnect = True
        return

    for next in graph[node]:
        if visit[next.node]:
            continue
        if next.weight < weight:
            continue
        dfs(next.node, weight)

N, M = map(int, sys.stdin.readline().strip().split())
graph = defaultdict(list)
weights = set()

for i in range(M):
    A, B, C = map(int, sys.stdin.readline().strip().split())
    graph[A].append(Node(B, C))
    graph[B].append(Node(A, C))
    weights.add(C)

T1, T2 = map(int, sys.stdin.readline().strip().split())

weights = list(weights)
weights.sort()

answer = 0
start = 0; end = len(weights) - 1;

while start <= end:
    mid = (start + end) // 2
    isConnect = False
    visit = [False] * (N + 1)
    dfs(T1, weights[mid])
    if isConnect:
        answer = max(answer, weights[mid])
        start = mid + 1 # 더 큰 중량이 가능함
    else:
        end = mid - 1

sys.stdout.write(str(answer))
