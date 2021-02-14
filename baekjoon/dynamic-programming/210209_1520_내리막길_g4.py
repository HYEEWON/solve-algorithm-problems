import sys

M, N = map(int, sys.stdin.readline().strip().split())
board = []
for m in range(M):
    board.append(list(map(int, sys.stdin.readline().strip().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
dp = [[-1 for i in range(N)] for i in range(M)]

def dfs(y, x, height):
    if y == M-1 and x == N-1:
        return 1
    if dp[y][x] != -1:
        return dp[y][x]

    dp[y][x] = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if nx<0 or ny<0 or nx>=N or ny>=M:
            continue
        if board[ny][nx] < height:
            dp[y][x] += dfs(ny, nx, board[ny][nx])
    return dp[y][x]

sys.stdout.write(str(dfs(0, 0, board[0][0])))
for i in range(4):
    print(dp[i])