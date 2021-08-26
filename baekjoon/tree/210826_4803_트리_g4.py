import sys
from collections import defaultdict

def dfs(n, previous):
    global cnt
    for node in tree[n]:
        if (node == previous): # 현재 노드와 이전 노드가 같다면
            continue
        if visit[node]: # 방문한 노드이면 == 트리가 아니면
            return False
        visit[node] = True
        if dfs(node, n) == False:
            return False
    return True

case = 1
while True:
    tree = defaultdict(list)
    cnt = 0
    # 정점 수, 간선 수
    n, m = map(int, sys.stdin.readline().strip().split())
    if n == 0 and m == 0:
            break

    for i in range(m):
        a, b = map(int, sys.stdin.readline().strip().split())
        tree[a].append(b)
        tree[b].append(a)

    visit = [False for i in range(n+1)]
    
    for i in range(1, n+1, 1):
        if not visit[i]:
            visit[i] = True
            if dfs(i, 0):
                cnt += 1
    
    if cnt > 1:
        sys.stdout.write("Case " + str(case) + ": A forest of " + str(cnt) + " trees.\n")
    elif cnt == 1:
        sys.stdout.write("Case " + str(case) + ": There is one tree.\n")
    else:
        sys.stdout.write("Case "  + str(case) + ": No trees.\n")

    case += 1