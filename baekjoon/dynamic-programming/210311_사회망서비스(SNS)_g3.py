#  현재 노드가 얼리어답터 -> 인접한 다음 노드 얼리어답터 x
# 현재 노드가 얼리어답터 x -> 인접한 다음 노드는 얼리어답터 or x

import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline())
tree = defaultdict(list)
for n in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

dp = [[0, 0] for j in range(N+1)] 
check = [True for j in range(N+1)]

def dfs(cur):
    check[cur] = False
    dp[cur][0] = 1
    dp[cur][1] = 0

    for i in tree[cur]:
        if check[i]:
            dfs(i)
            dp[cur][0] += dp[i][1]
            dp[cur][1] += max(dp[i][0], dp[i][1])

dfs(1)
print(N-max(dp[1][0], dp[1][1]))

#(*) 메모리 초과
'''import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline())
tree = defaultdict(list)
for n in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

dp = [[-1, -1] for j in range(N+1)]
# 0: 자신은 얼리X # 1: 자신도 얼리어답터

def solution(prev, cur, state):
    if dp[cur][state] != -1:
        return dp[cur][state]
    
    if state:
        dp[cur][state] = 1
    else:
        dp[cur][state] = 0

    for i in range(len(tree[cur])):
        nexts = tree[cur][i]
        if prev == nexts:
            continue
        if state:
            dp[cur][state] += min(solution(cur, nexts, 1), solution(cur, nexts, 0))
        else:
            dp[cur][state] += solution(cur, nexts, 1)
    return dp[cur][state]

print(min(solution(-1, 1, 1), solution(-1, 1, 0)))'''