import sys
from copy import deepcopy

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]

board = [[[0 for i in range(4)] for j in range(4)] for k in range(2)]

for i in range(4):
    tmp = list(map(int, sys.stdin.readline().strip().split()))
    idx = 0
    for j in range(0, 7, 2):
        board[0][i][idx] = tmp[j]
        board[1][i][idx] = tmp[j+1] - 1
        idx += 1

def find_fish(x, tmp_board):
    for i in range(4):
        for j in range(4):
            if tmp_board[0][i][j] == x:
                return [i, j], tmp_board[1][i][j]
    return None, None

def move_fish(y, x):
    global board
    for i in range(1, 17):
        fish, fish_dir = find_fish(i, board)
        if fish != None:
            for q in range(8):
                ny = fish[0] + dy[fish_dir]
                nx = fish[1] + dx[fish_dir]
                if 0 <= nx < 4 and 0 <= ny < 4 and [y, x] != [ny, nx]:
                    board[0][fish[0]][fish[1]], board[0][ny][nx] = board[0][ny][nx], board[0][fish[0]][fish[1]]
                    board[1][fish[0]][fish[1]], board[1][ny][nx] = board[1][ny][nx], fish_dir
                    break
                fish_dir = (fish_dir + 1) % 8

answer = 0

def dfs(y, x, shark_dir, total):
    global answer, board

    move_fish(y, x)

    while True:
        ny = y + dy[shark_dir]
        nx = x + dx[shark_dir]
        if not 0 <= ny < 4 or not 0 <= nx < 4:
            answer = max(answer, total)
            return
        if board[0][ny][nx] == -1: # 빈칸이면 그냥 이동
            y, x = ny, nx
            continue
        
        tmp_board = deepcopy(board)
        tmp = board[0][ny][nx]
        board[0][ny][nx] = -1
        dfs(ny, nx, board[1][ny][nx], tmp+total)
        board = deepcopy(tmp_board)
        x, y = nx, ny

answer += board[0][0][0]
board[0][0][0] = -1
dfs(0, 0, board[1][0][0], answer)
print(answer)