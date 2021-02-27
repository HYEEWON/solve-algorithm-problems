import sys
from collections import defaultdict, deque

n = int(sys.stdin.readline().strip())
tree = defaultdict(list)

for i in range(n-1):
    parent, child, weight = map(int, sys.stdin.readline().strip().split())
    tree[parent].append([child, weight])
    tree[child].append([parent, weight])

answer = 0
endNode = 0

def bfs(node, w):
    global answer, endNode

    visit = [0 for i in range(n+1)]
    q = deque()
    q.append([node, w])
    visit[node] = 1

    while q:
        node, w = q.popleft()
        for i in tree[node]:
            if visit[i[0]] == 0:
                visit[i[0]] = 1
                q.append([i[0], i[1]+w])

                if i[1]+w > answer:
                    answer = i[1]+w
                    endNode = i[0]

bfs(1, 0)
bfs(endNode, 0)
print(answer)