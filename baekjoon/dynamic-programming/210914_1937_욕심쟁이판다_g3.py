import sys
sys.setrecursionlimit(10**9)
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

answer = 0
def dfs(y, x):
    global answer, N
    dp[y][x] = 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if not 0<=ny<N or not 0<=nx<N:
            continue
        if board[ny][nx] > board[y][x]:
            if dp[ny][nx]:
                dp[y][x] = max(dp[y][x], dp[ny][nx]+1)
            else:
                dp[y][x] = max(dp[y][x], dfs(ny, nx)+1)
    return dp[y][x]

N = int(sys.stdin.readline())

board = []
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().strip().split())))

dp = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    for j in range(N):
        if not dp[i][j]:
            answer = max(answer, dfs(i, j))

sys.stdout.write(str(answer)+"\n")