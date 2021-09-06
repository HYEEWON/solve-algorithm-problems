import sys

T = int(sys.stdin.readline())

# dp[n][i]: 마지막 수가 i일 때, 1, 2, 3의 합으로 정수 n을 만드는 경우의 수
dp = [[0 for i in range(4)] for j in range(100001)]

dp[1][1] = dp[2][2] = dp[3][3] = dp[3][1] = dp[3][2] = 1
for i in range(4, 100001):
    dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % 1000000009
    dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % 1000000009
    dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % 1000000009

for t in range(T):
    n = int(sys.stdin.readline())
    sys.stdout.write(str(sum(dp[n]) % 1000000009) + '\n')