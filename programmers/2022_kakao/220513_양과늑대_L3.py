# dfs

# 풀이
# 방문할 수 있는 노드를 담은 배열로 다음 노드를 방문함

from collections import defaultdict
from copy import deepcopy

answer = 0

def dfs(info, tree, node, available, cnt, visit):
    global answer

    if cnt[0] <= cnt[1]:
        return  # 양이 잡아먹힘
    answer = max(answer, cnt[0])
    for n in tree[node]:
        if not visit[n]:
            available.append(n)

    for next in available:
        if visit[next]:
            continue
        tmp = deepcopy(available)
        tmp.remove(next)
        cnt[info[next]] += 1
        visit[next] = True
        dfs(info, tree, next, tmp, cnt, visit)
        visit[next] = False
        cnt[info[next]] -= 1


def solution(info, edges):
    global answer
    tree = defaultdict(list)

    for edge in edges:
        tree[edge[0]].append(edge[1])
        tree[edge[1]].append(edge[0])

    visit = [False for i in range(len(info))]
    visit[0] = True
    dfs(info, tree, 0, [], [1, 0], visit)

    return answer