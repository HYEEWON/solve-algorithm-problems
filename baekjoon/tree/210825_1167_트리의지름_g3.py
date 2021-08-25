import sys
from collections import defaultdict, deque

max_cost = 0

def bfs(n):
    global max_cost
    max_node = 1;

    visit = [0 for i in range(V+1)]
    q = deque()
    q.append((n, 0))
    visit[n] = 1
    while q:
        node, cost = q.popleft()

        if cost > max_cost:
            max_node = node
            max_cost = cost

        for t in tree[node]:
            if visit[t[0]] == 1:
                continue
            visit[t[0]] = 1
            q.append((t[0], cost + t[1]))
    return max_node

tree = defaultdict(list)
V = int(sys.stdin.readline())

for v in range(V):
    tmp = list(map(int, sys.stdin.readline().strip().split()))

    for i in range(1, len(tmp)-2, 2):
        tree[tmp[0]].append((tmp[i], tmp[i+1]))

max_node = bfs(1)
max_node = bfs(max_node)

sys.stdout.write(str(max_cost))