import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().strip().split()))

dp = [0 for i in range(N)]
answer = 0

for i in range(N):
    dp[i] = A[i]
    for j in range(i):
        if A[i] > A[j] and dp[i] < (dp[j] + A[i]):
            dp[i] = dp[j] + A[i]
            answer = max(answer, dp[i])
sys.stdout.write(str(answer))
