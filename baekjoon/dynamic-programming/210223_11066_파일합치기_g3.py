import sys

T = int(sys.stdin.readline())

for t in range(T):
    K = int(sys.stdin.readline())
    files = list(map(int, sys.stdin.readline().strip().split()))

    sums = [0]*(K+1)

    for i in range(1, K+1):
        sums[i] = sums[i-1] + files[i-1]
    dp = [[0 for i in range(K+1)] for j in range(K+1)]
    # dp[i][j]  = i번째 장부터 j번째 장까지 합치는데 드는 최소한의 비용
    print(sums)
    for i in range(1, K):
        for x in range(1, K-i+1):
            y = x + i
            dp[x][y] = sys.maxsize

            for m in range(x, y):
                dp[x][y] = min(dp[x][y], dp[x][m]+dp[m+1][y]+sums[y]-sums[x-1])
    for i in range(K):
        print(dp[i])
    print(dp[1][K])