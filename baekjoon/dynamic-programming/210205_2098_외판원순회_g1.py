import sys

# 출발점 == 도착점이기 때문에 처음 출발지의 위치는 상관X
# 한번 간 상태는 저장하여 다시가지 않음.
# 상태 표현: 내가 있는 위치 + 내가 거쳐온 곳 -> 비트 계산

N = int(sys.stdin.readline().rstrip())
W = [] #W[i][j]: 도시 i에서 도시 j로 가기 위한 비용
for i in range(N):
    W.append(list(map(int, sys.stdin.readline().rstrip().split())))

dp = [[0 for i in range(1<<N)] for j in range(N)]

def dfs(now, visit):
    global N
    if (visit == (1<<N)-1):
        return W[now][0] if W[now][0] > 0 else sys.maxsize

    if dp[now][visit]:
        return dp[now][visit]

    cost = sys.maxsize    
    for i in range(1, N):
        if W[now][i] > 0 and (visit&(1<<i) == 0):
            cost = min(cost, dfs(i, (visit | (1<<i))) + W[now][i])
    dp[now][visit] = cost
    return cost

sys.stdout.write(str(dfs(0, 1<<0))) # 1번 부터 순회

