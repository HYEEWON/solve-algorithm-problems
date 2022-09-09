# DFS
# 방문할 수 있는 노드들을 계속 가지고 있어야 함

from collections import defaultdict
from copy import deepcopy

answer = 0
def dfs(info, tree, node, cnt, visit, available):
    global answer
    if cnt[0] <= cnt[1]:
        return
    answer = max(answer, cnt[0])
    for t in tree[node]:
        if not visit[t]:
            available.append(t)

    for t in available:
        tmp = deepcopy(available)
        tmp.remove(t)
        cnt[info[t]] += 1
        visit[t] = True
        dfs(info, tree, t, cnt, visit, tmp)
        visit[t] = False
        cnt[info[t]] -= 1

def solution(info, edges):
    global answer

    tree = defaultdict(list)
    for edge in edges:
        tree[edge[0]].append(edge[1])
        tree[edge[1]].append(edge[0])

    visit = [False for i in range(len(tree.keys()))]
    visit[0] = True
    dfs(info, tree, 0, [1, 0], visit, [])

    return answer