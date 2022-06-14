# 완전 탐색, 백트랙킹

T = int(input())

dx = [-1, 1, 0, 0]  # 좌, 우
dy = [0, 0, 1, -1]  # 하, 상


def dfs(y, x, cnt, chg):
    global ans
    ans = max(ans, cnt)
    for k in range(4):
        nx = dx[k] + x
        ny = dy[k] + y
        if nx < 0 or ny < 0 or nx > len(board) - 1 or ny > len(board) - 1 or visit[ny][nx]:
            continue

        if board[ny][nx] < board[y][x]:
            visit[ny][nx] = 1
            dfs(ny, nx, cnt + 1, chg)
            visit[ny][nx] = 0
        elif board[ny][nx] >= board[y][x] and chg == False:
            tmp = board[ny][nx]
            for i in range(1, K + 1, 1):
                board[ny][nx] = board[ny][nx] - 1
                if board[ny][nx] < board[y][x]:
                    visit[ny][nx] = 1
                    chg = True
                    dfs(ny, nx, cnt + 1, chg)
                    chg = False
                    visit[ny][nx] = 0
            board[ny][nx] = tmp


for t in range(1, T + 1, 1):
    N, K = map(int, input().split())
    ans = 0
    board = []
    max_board = 0  # 보드의 최대값
    for n in range(N):
        line = list(map(int, input().split()))
        max_board = max(max_board, max(line))
        board.append(line)

    for i in range(len(board)):
        for j in range(len(board)):
            visit = [[0 for a in range(len(board))] for b in range(len(board))]
            if board[i][j] == max_board:
                visit[i][j] = 1
                dfs(i, j, 1, False)
    print('#' + str(t) + ' ' + str(ans))