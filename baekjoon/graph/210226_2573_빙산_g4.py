import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())

board = []
for n in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(y, x, n):
    global visit
    q = deque()
    q.append([y, x])
    visit[y][x] = n

    while q:
        y, x = q.popleft()
        cnt = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx<0 or ny<0 or nx>=M or ny>=N:
                continue
            if board[ny][nx] <= 0 and visit[ny][nx] == 0:
                cnt += 1
        board[y][x] -= cnt
        if board[y][x] < 0:
            board[y][x] = 0

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx<0 or ny<0 or nx>=M or ny>=N:
                continue
            if board[ny][nx] > 0 and visit[ny][nx] == 0:
                visit[ny][nx] = n
                q.append([ny, nx])

answer = 0
while True:
    cnt = 1
    visit = [[0 for i in range(M)] for j in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0 and visit[i][j] == 0:
                bfs(i, j, cnt)
                cnt += 1

    answer += 1
    if cnt > 2:
        break
    flag = 0
    for i in range(N):
        flag += board[i].count(0)
    if flag == N*M:
        answer = 1
        break
sys.stdout.write(str(answer-1))