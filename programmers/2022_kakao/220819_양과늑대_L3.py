from collections import defaultdict
from copy import deepcopy

answer = 0
def dfs(info, tree, node, cnt, visit, available):
    global answer
    if cnt[0] <= cnt[1]:
        return
    answer = max(answer, cnt[0])
    print(node, cnt, available, "  #########")
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
        print(node, cnt, available)


def solution(info, edges):
    global answer

    tree = defaultdict(list)
    for edge in edges:
        tree[edge[0]].append(edge[1])
        tree[edge[1]].append(edge[0])
    print(tree)
    visit = [False for i in range(len(tree.keys()))]
    visit[0] = True
    dfs(info, tree, 0, [1, 0], visit, [])

    return answer

print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))