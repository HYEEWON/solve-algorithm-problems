from collections import deque


def bfs(y, x):
    q = deque([[y, x]])
    visit[y][x] = arr[y][x]
    while q:
        y = q[0][0]
        x = q[0][1]
        q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if N > nx >= 0 and N > ny >= 0:
                if visit[ny][nx] > visit[y][x] + arr[ny][nx]:
                    visit[ny][nx] = visit[y][x] + arr[ny][nx]
                    q.append([ny, nx])


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

T = int(input())
for t in range(T):
    N = int(input())
    arr = []
    for n in range(N):
        line = list(map(int, input()))
        arr.append(line)
    visit = [[float('inf') for i in range(N)] for j in range(N)]
    bfs(0, 0)
    print('#' + str(t + 1) + ' ' + str(visit[N - 1][N - 1]))