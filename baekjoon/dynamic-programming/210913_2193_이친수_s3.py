import sys

N = int(sys.stdin.readline())
dp = [0 for i in range(N+1)]

dp[1] = 1

if N > 1:
    dp[2] = 1

for i in range(3, N+1):
	dp[i] = dp[i-1] + dp[i-2]

sys.stdout.write(str(dp[N]))