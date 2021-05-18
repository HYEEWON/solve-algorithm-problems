import sys
from collections import defaultdict, deque

N, M, k = map(int, sys.stdin.readline().split())
board = [[], []]
shark = [[[] for i in range(M)], []]
for i in range(N):
    ins = list(map(int, sys.stdin.readline().strip().split()))
    board[0].append(ins)
    board[1].append([0 for l in range(N)])
    for j in range(len(ins)):
        if board[0][i][j] != 0:
            board[1][i][j] = k
            shark[0][board[0][i][j]-1] = [i, j]

shark[1] = list(map(int, sys.stdin.readline().strip().split()))
order = defaultdict(list)
for i in range(1, M+1):
    tmp = []
    for j in range(4):
        tmp.append(list(map(int, sys.stdin.readline().strip().split())))
    order[i] = tmp

dy = [0, -1, 1, 0, 0] # 위 아래 왼 오
dx = [0, 0, 0, -1, 1]

shark_flag = [1 for i in range(M)]

def update_board():
    for i in range(N):
        for j in range(N):
            if board[0][i][j] > 0:
                board[1][i][j] -= 1
                if board[1][i][j] == 0:
                    board[0][i][j] = 0

def move_shark(n):
    global k
    flag = 0;

    y, x = shark[0][n-1][0], shark[0][n-1][1]
    for i in range(4):
        ny = y + dy[order[n][shark[1][n-1]-1][i]]
        nx = x + dx[order[n][shark[1][n-1]-1][i]]
        if not 0<=nx<N or not 0<=ny<N:
            continue
        if board[1][ny][nx] == 0:
            shark[0][n-1] = [ny, nx]
            shark[1][n-1] = order[n][shark[1][n-1]-1][i]
            tmp_cnt_shark[(ny, nx)].append(n)
            flag = 5;
            break;
        elif board[0][ny][nx] == n and flag == 0:
            flag = order[n][shark[1][n-1]-1][i]
    if 0 < flag < 5:
        ny = y + dy[flag]
        nx = x + dx[flag]
        shark[0][n-1] = [ny, nx]
        shark[1][n-1] = flag
        tmp_cnt_shark[(ny, nx)].append(n)

answer = 1
while answer <= 1000:
    tmp_cnt_shark = defaultdict(list)
    for n in range(1, M+1):
        if shark_flag[n-1] == 1:
            move_shark(n)

    for key in tmp_cnt_shark.keys():
        if len(tmp_cnt_shark[key]) > 1:
            tmp_cnt_shark[key].sort()
            for i in range(1, len(tmp_cnt_shark[key])):
                shark_flag[tmp_cnt_shark[key][i]-1] = 0

    update_board()
    for n in range(1, M+1):
        if shark_flag[n-1] == 1:
            board[0][shark[0][n-1][0]][shark[0][n-1][1]] = n
            board[1][shark[0][n-1][0]][shark[0][n-1][1]] = k  
    if shark_flag.count(1) == 1:
        break
    answer += 1 

if answer <= 1000:
    print(answer)
else:
    print(-1)