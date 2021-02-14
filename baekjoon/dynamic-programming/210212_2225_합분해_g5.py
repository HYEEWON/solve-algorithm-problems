import sys

N, K = map(int, sys.stdin.readline().strip().split())

# dp[i][j] = dp[i-0][j-1] + dp[i-1][j-1] + ... + dp[i-i][j-1]
# dp[i][j]: i를 만들기 위해 j개의 숫자를 더함
dp = [[0 for j in range(K+1)] for i in range(N+1)]
for i in range(N+1):
    dp[i][1] = 1;

for j in range(2, K+1):
    for i in range(N+1):
        for k in range(i+1): 
            dp[i][j] = (dp[i][j] + dp[i-k][j-1]) % 1000000000

sys.stdout.write(str(dp[N][K])+'\n')