import sys

n = int(sys.stdin.readline().strip())

box = list(map(int, sys.stdin.readline().strip().split()))

dp = [0 for i in range(n)]
dp[0] = 1
answer = 0

for i in range(1, n):
    for j in range(i):
        if (box[i] > box[j]):
            dp[i] = max(dp[i], dp[j])
    dp[i] += 1
    answer = max(answer, dp[i])
print(answer)
