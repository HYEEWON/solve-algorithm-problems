import sys

#(*)
def f(N, M, K, NM): # a를 i-1개, z를 j개 사용해서 만들 수 있는 경우의 수
    print(N, M, K, NM, end=' ')
    if N+M <= 0:
        return
    if N == 0:
        sys.stdout.write('z')
        f(N, M-1, K-dp[N+M-1][M], NM-1)
    elif M == 0:
        sys.stdout.write('a')
        f(N-1, M, K, NM-1)
    elif dp[N+M-1][M] >= K:
        print(dp[N+M-1][M], K)
        sys.stdout.write('a')
        f(N-1, M, K, NM-1)
    else:
        print(dp[N+M-1][M], K)
        sys.stdout.write('z')
        f(N, M-1, K-dp[N+M-1][M], NM-1)

# N+MCM: 전체 문자의 개수에서 'z'가 들어갈 M개의 위치를 고름
N, M, K = map(int, input().split())

dp = [[0 for i in range(M+1)] for j in range(N+M+1)]

for i in range(1, N+M+1): # 파스칼 삼각형
    for j in range(min(i, M)+1):
        if (j == 0 or i == j):
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

if dp[N+M][M] < K:
    print(-1)
else:
    f(N, M, K, N+M)