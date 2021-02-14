import sys, copy
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
board = []
virus = []
wall = 3

for n in range(N):
    board.append(list(map(int, sys.stdin.readline().strip().split())))
    for m in range(M):
        if board[n][m] == 2:
            virus.append([n, m])
        if board[n][m] == 1:
            wall += 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(wall):
    tmp = copy.deepcopy(board)
    q = deque()
    cnt = 0
    for v in virus:
        q.append([v[0], v[1]])
        cnt += 1
        tmp[v[0]][v[1]] = 2

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx<0 or ny<0 or nx>=M or ny>=N:
                continue
            if tmp[ny][nx] == 0:
                tmp[ny][nx] = 2
                cnt += 1
                q.append([ny, nx])
    return cnt + wall

answer = N*M
def select(cnt):
    global answer   
    if cnt == 3:
        answer = min(answer, bfs(wall))
        return
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                select(cnt+1)
                board[i][j] = 0
    return

select(0)
answer = N*M - answer
sys.stdout.write(str(answer))