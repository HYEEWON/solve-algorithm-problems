'''import sys

n, k = map(int, sys.stdin.readline().split())
coins = []
for c in range(n):
    coins.append(int(sys.stdin.readline()))
coins.sort()

dp = [[0 for i in range(n+1)] for j in range(k+1)]
dp[0] = [1 for i in range(n+1)]
for i in range(1, k+1):
    for j in range(1, n+1):
        if coins[j-1] <= i:
            dp[i][j] = dp[i][j-1]+dp[i-coins[j-1]][j]
        else:
            dp[i][j] = dp[i][j-1]

sys.stdout.write(str(dp[k][n]))'''

import sys

n, k = map(int, sys.stdin.readline().split())
coins = []
for c in range(n):
    coins.append(int(sys.stdin.readline()))
coins.sort()

dp = [0 for j in range(k+1)]
dp[0] = 1
for coin in coins:
    for j in range(coin, k+1):
        dp[j] += dp[j-coin]

sys.stdout.write(str(dp[k]))