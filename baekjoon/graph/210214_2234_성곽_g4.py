import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())

board = []
rooms = {}

for m in range(M):
    board.append(list(map(int, sys.stdin.readline().strip().split())))

dx = [0, 1, 0, -1] # 서(1), 동(4)
dy = [1, 0, -1, 0] # 남(8), 북(2)
# 남 동 북 서
def bfs(m, n, room):
    global N, M
    q = deque()
    q.append([m, n])
    visit[m][n] = room
    ret = 1
    
    while q:
        y, x = q.popleft()
        if board[y][x] == 15:
            visit[y][x] = room
            return ret
        bit = 16
        for i in range(4):
            bit = bit >> 1
            if not board[y][x] & bit:
                ny = y + dy[i]
                nx = x + dx[i]
                if visit[ny][nx] == 0:
                    visit[ny][nx] = room
                    ret += 1
                    q.append([ny, nx])
    return ret

visit = [[0 for i in range(N)] for j in range(M)]

answer = [0, 0, 0]
for m in range(M):
    for n in range(N):
        if visit[m][n] == 0:
            answer[0] += 1
            ret = bfs(m, n, answer[0])
            answer[1] = max(answer[1], ret)
            rooms[answer[0]] = ret

for m in range(M):
    for n in range(N):
        bit = 8
        for k in range(4):
            if board[m][n] & (bit):
                ny = m + dy[k]
                nx = n + dx[k]
                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    bit = bit>>1
                    continue
                if visit[m][n] != visit[ny][nx]:
                    answer[2] = max(answer[2], rooms[visit[m][n]]+rooms[visit[ny][nx]])
            bit = bit>>1

for i in range(3):
    sys.stdout.write(str(answer[i])+'\n')