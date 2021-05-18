import sys
from collections import deque

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

board = [[0 for i in range(N)] for j in range(N)]

for k in range(K):
    y, x = map(int, sys.stdin.readline().split())
    board[y-1][x-1] = 1

L = int(sys.stdin.readline())

answer = 0
move = deque()
for l in range(L):
    X, C = sys.stdin.readline().split()
    move.append([X, C])

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

direction = 0

q = deque()
q.append([0, 0])
board[0][0] = 2

while q:
    y, x = q[-1]
    ny = y + dy[direction]
    nx = x + dx[direction]
    answer += 1

    if len(move) > 0 and answer == int(move[0][0]):
        X, C = move.popleft()
        if C == 'D':
            direction = (direction+1) % 4
        else:
            if direction == 0:
                direction = 3
            else:
                direction = (direction-1) % 4

    if not 0 <= ny < N or not 0 <= nx < N:
        break
    if board[ny][nx] == 2:
        break
    elif board[ny][nx] == 1:
        board[ny][nx] = 2    
        q.append([ny, nx])
    else:
        board[ny][nx] = 2
        q.append([ny, nx])
        out_y, out_X = q.popleft()
        board[out_y][out_X] = 0

sys.stdout.write(str(answer))