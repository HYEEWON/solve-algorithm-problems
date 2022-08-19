# DP

# 최대한 많은 인원이 회의를 함
# 임의의 회의 K(1≤ K ≤ N)는 회의 K − 1과 회의 K + 1과는 회의 시간이 겹치고 다른 회의들과는 회의 시간이 겹치지 않음

import sys

N = int(sys.stdin.readline())
meetings = [list(map(int, sys.stdin.readline().strip().split())) for i in range(N)]

dp = [0 for i in range(N+1)]
dp[1] = meetings[0][2]

for i in range(2, N+1):
    dp[i] = max(dp[i-2]+meetings[i-1][2], dp[i-1])

sys.stdout.write(str(dp[-1]))
