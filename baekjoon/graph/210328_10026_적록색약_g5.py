from collections import deque

N = int(input())

board = []
for i in range(N):
    board.append(list(input()))

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(y, x, k):
    answer[k] += 1
    q = deque()
    q.append([y, x])

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx<0 or ny<0 or nx>=N or ny>=N:
                continue
            if visit[k][ny][nx] == 1:
                continue
            if board[y][x] == board[ny][nx]:
                visit[k][ny][nx] = 1
                q.append([ny, nx])
            if k == 1:
                if board[y][x] in ['R', 'G'] and board[ny][nx] in ['R', 'G']:
                    visit[k][ny][nx] = 1
                    q.append([ny, nx])

visit = [[[0 for i in range(N)] for j in range(N)] for k in range(2)]
answer = [0, 0]
for k in range(2):
    for i in range(N):
        for j in range(N):
            if visit[k][i][j] == 0:
                visit[k][i][j] = 1
                bfs(i, j, k)

print(answer[0], answer[1])