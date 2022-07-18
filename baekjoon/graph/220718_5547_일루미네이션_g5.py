# BFS

import sys
from collections import deque

dy_o = [-1, 0, 1, 1, 0, -1]
dx_o = [1, 1, 1, 0, -1, 0]

dy_e = [-1, 0, 1, 1, 0, -1]
dx_e = [0, 1, 0, -1, -1, -1]

W, H = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for i in range(H)]
answer = 0
visit = [[False for i in range(W+1)] for j in range(H+1)]

def bfs1(y, x):
    global visit, W, H, answer
    visit[y][x], board[y-1][x-1] = True, 2
    q = deque()
    q.append((y, x))

    while q:
        y, x = q.popleft()
        for i in range(6):
            if y % 2 == 0:
                ny, nx = y + dy_e[i], x + dx_e[i]
            else:
                ny, nx = y + dy_o[i], x + dx_o[i]

            if not 1<=ny<=H or not 1<=nx<=W:
                continue
            if visit[ny][nx] or board[ny-1][nx-1] == 1:
                continue
            visit[ny][nx] = True
            q.append((ny, nx))
            board[ny-1][nx-1] = 2

def bfs2(y, x):
    global visit, W, H, answer
    visit[y][x] = True
    q = deque()
    q.append((y, x))

    while q:
        y, x = q.popleft()
        cnt = 0
        for i in range(6):
            if y % 2 == 0:
                ny, nx = y + dy_e[i], x + dx_e[i]
            else:
                ny, nx = y + dy_o[i], x + dx_o[i]

            if not 1<=ny<=H or not 1<=nx<=W or board[ny-1][nx-1] == 2:
                continue
            if visit[ny][nx]:
                cnt += 1
                continue
            visit[ny][nx] = True
            q.append((ny, nx))
            cnt += 1
        answer += (6-cnt)

for i in range(1, H+1):
    for j in range(1, W+1):
        if i in [1, H] or j in [1, W]:
            if not visit[i][j] and board[i-1][j-1] == 0:
                bfs1(i, j)

for i in range(1, H+1):
    for j in range(1, W+1):
        if not visit[i][j] and board[i-1][j-1] == 1:
            bfs2(i, j)

print(answer)