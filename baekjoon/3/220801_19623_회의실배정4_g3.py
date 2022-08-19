# DP

# 가장 많은 사람이 회의에 참석
# 회의 종료 시간으로 정렬
# 시작 시간과 종료시간을 1차원 배열로 풀어 DP 진행

import sys

N = int(sys.stdin.readline())
meetings = [list(map(int, sys.stdin.readline().strip().split())) for i in range(N)]
meetings.sort(key=lambda x: (x[1], x[0], -x[2])) # 회의 종료 시간으로 정렬

times, time_index = [], {}
for m in meetings:
    times.append(m[0])
    times.append(m[1])
times.sort()

for i, t in enumerate(times):
    time_index[t] = i

dp = [0 for i in range(len(times))]
end = 0 # 진행한 미팅 인덱스

for s in range(1, len(times)):
    if times[s] == meetings[end][1]:
        dp[s] = max(dp[s-1], dp[time_index[meetings[end][0]]]+meetings[end][2])
        end += 1
    else:
        dp[s] = dp[s-1]

sys.stdout.write(str(dp[-1]))
