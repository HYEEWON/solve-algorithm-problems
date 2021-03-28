import sys

N, M = map(int, sys.stdin.readline().split())
r, c, direction = map(int, sys.stdin.readline().split())
board = []
for n in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

visit = [[0 for i in range(M)] for j in range(N)]

# 왼쪽
dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

#후진
by = [1, 0, -1, 0]
bx = [0, -1, 0, 1]

def move(direction):
    if direction == 0:
        return 3
    elif direction == 1:
        return 0
    elif direction == 2:
        return 1
    else:
        return 2

answer = 0
def dfs(y, x, direction):
    global answer
    if board[y][x] == 0:
        board[y][x] = 2
        answer += 1

    for i in range(4):
        ny = y+dy[direction]
        nx = x+dx[direction]
        if nx<0 or nx>=M or ny<0 or ny>=N:
            continue
        if board[ny][nx] == 0:
            dfs(ny, nx, move(direction))
            return
        else:
            direction = move(direction)
    ny = y+by[direction]
    nx = x+bx[direction]
    if nx<0 or nx>=M or ny<0 or ny>=N:
        pass
    if board[ny][nx] == 1:
        return
    dfs(ny, nx, direction)
    return
    
dfs(r, c, direction)
print(answer)