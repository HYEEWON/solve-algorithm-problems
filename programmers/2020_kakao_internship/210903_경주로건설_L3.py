from collections import deque
import sys

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
dr = [0, 0, 1, 1] # 방향 - 가로: 0, 세로: 1

def bfs(board, dir, v):
    visit = [[sys.maxsize for i in range(len(board))] for j in range(len(board))]
    N = len(board)

    q = deque()
    q.append([v[0], v[1], dir, 0])
    visit[0][0] = 0

    while q:
        y, x, dir, cost = q.popleft()
        if y == N-1 and x == N-1:
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if not 0<=nx<N or not 0<=ny<N or board[ny][nx] == 1:
                continue
            if dir == dr[i] and visit[ny][nx] > cost+100:
                visit[ny][nx] = cost + 100
                q.append([ny, nx, dr[i], cost + 100])
            elif dir != dr[i] and visit[ny][nx] > cost+600:
                visit[ny][nx] = cost + 600
                q.append([ny, nx, dr[i], cost + 600])
    return visit[N-1][N-1]


def solution(board):
    return min(bfs(board, 0, (0, 0)), bfs(board, 1, (0, 0)))

print(solution([[0,0,0],[0,0,0],[0,0,0]]))