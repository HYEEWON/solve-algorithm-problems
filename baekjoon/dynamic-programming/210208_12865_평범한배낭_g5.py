import sys

N, K = map(int, sys.stdin.readline().strip().split())
array = [[0, 0]]
dp = [[0 for i in range(K+1)] for j in range(N+1)]

for i in range(N):
    array.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        if (array[i][0] <= j):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-array[i][0]]+array[i][1])
        else:
            dp[i][j] = dp[i-1][j]
    print(dp[i])

sys.stdout.write(str(dp[N][K]))