import sys

dy = [0, 0, 0, -1, 1]
dx = [0, 1, -1, 0, 0]

dice = [0, 0, 0, 0, 0, 0, 0] # 위, 앞, 아래, 뒤, 왼, 오른

N, M, y, x, K = map(int, sys.stdin.readline().split())

board = []
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().strip().split())))

move = list(map(int, sys.stdin.readline().strip().split()))

for m in move:
    ny, nx = y + dy[m], x + dx[m]
    if not 0<=ny<N or not 0<=nx<M:
        continue
    y, x = ny, nx

    if m == 4: # 아래
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]
    elif m == 3: # 위
        dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]
    elif m == 2: # 오른
        dice[0], dice[5], dice[2], dice[4] = dice[4], dice[0], dice[5], dice[2]
    else: # 왼
        dice[0], dice[5], dice[2], dice[4] = dice[5], dice[2], dice[4], dice[0]

    if board[y][x] != 0:
        dice[2] = board[y][x]
        board[y][x] = 0
    else:
        board[y][x] = dice[2]

    # 윗면 출력
    sys.stdout.write(str(dice[0]) + "\n")