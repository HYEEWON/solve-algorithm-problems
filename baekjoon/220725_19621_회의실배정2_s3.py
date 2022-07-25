# DFS, 백트래킹

# 최대한 많은 인원이 회의를 함
# 임의의 회의 K(1≤ K ≤ N)는 회의 K − 1과 회의 K + 1과는 회의 시간이 겹치고 다른 회의들과는 회의 시간이 겹치지 않음

import sys

N = int(sys.stdin.readline())
meetings = [list(map(int, sys.stdin.readline().strip().split())) for i in range(N)]

def dfs(idx, cnt):
    global meetings, N
    if idx >= N:
        return cnt

    return max(dfs(idx+1, cnt), # idx 번지 회의를 진행하지 않음
        dfs(idx+2, cnt+meetings[idx][2])) # idx 번지 회의를 진행

sys.stdout.write(str(dfs(0, 0)))



