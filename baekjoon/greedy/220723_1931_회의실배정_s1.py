# Greedy

# 회의가 끝나는 시간을 기준으로 오름차순 정렬
# 최대한 많은 회의 진행 가능

import sys

N = int(sys.stdin.readline())
meetings = [list(map(int, sys.stdin.readline().strip().split())) for i in range(N)]
meetings.sort(key=lambda x: (x[1], x[0]))

answer, end = 0, 0

for m in meetings:
    if m[0] >= end:
        answer += 1
        end = m[1]

sys.stdout.write(str(answer))