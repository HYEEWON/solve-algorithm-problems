import sys

T = int(sys.stdin.readline())

dp = [[1]*(31) for i in range(31)]

for m in range(1, 31):
    for n in range(1, 31):
        if m < n:
            break
        if m != n:
            dp[m][n] = dp[m-1][n-1] + dp[m-1][n]

for t in range(T):
    N, M = map(int, sys.stdin.readline().split())

    sys.stdout.write(str(dp[M][N]) + "\n")