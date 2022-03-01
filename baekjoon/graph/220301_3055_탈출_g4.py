from collections import deque
import sys

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

answer = 0
gy, gx, sy, sx = 0, 0, 0, 0

R, C = map(int, sys.stdin.readline().split())
forest = []

for i in range(R):
    forest.append(list(sys.stdin.readline().strip()))
    for idx in range(C):
        if forest[i][idx] == 'D':
            gy, gx = i, idx
            break
        elif forest[i][idx] == 'S':
            sy, sx = i, idx
            break


def water_bfs():
    global answer, R, C
    q = deque()

    for y in range(R):
        for x in range(C):
            if forest[y][x] == '*':
                q.append((y, x))

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if not 0 <= ny < R or not 0 <= nx < C:
                continue
            if forest[ny][nx] not in ['D', 'X']:
                forest[ny][nx] = '*'

def bfs(sy, sx):
    global answer, R, C

    q = deque()
    visit = [[False for i in range(C)] for j in range(R)]

    q.append((sy, sx, 0))
    visit[sy][sx] = True
    t, tmp = 1, 0

    while q:
        sy, sx, cnt = q.popleft()

        if forest[sy][sx] == 'D':
            return cnt
        if forest[sy][sx] == '*':
            continue

        t -= 1
        if t <= 0:
            water_bfs()
            t, tmp = tmp, 0

        for i in range(4):
            ny = sy + dy[i]
            nx = sx + dx[i]

            if not 0 <= ny < R or not 0 <= nx < C:
                continue
            if forest[ny][nx] not in ['X', '*'] and not visit[ny][nx]:
                visit[ny][nx] = True

                q.append((ny, nx, cnt+1))
                tmp += 1

    return 'KAKTUS'


sys.stdout.write(str(bfs(sy, sx)))