import sys, heapq

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().strip().split())) for i in range(N)]
q = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            heapq.heappush(q, (0, i, j))
            board[i][j] = 0

dy = [0, 1, -1, 0]
dx = [-1, 0, 0, 1]
visit = [[0 for i in range(N)] for j in range(N)]

def bfs():
    global q, visit
    size, eat, distance = 2, 0, 0
    
    while q:
        dist, y, x = heapq.heappop(q)

        if 0 < board[y][x] < size:
            eat += 1
            board[y][x] = 0
            if eat == size:
                size += 1
                eat = 0
            distance += dist

            dist = 0
            q = []
            visit = [[0]*N for _ in range(N)]

        for i in range(4):
            nd, ny, nx = dist+1, y+dy[i], x+dx[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if 0 < board[ny][nx] > size or visit[ny][nx]:
                continue
            visit[ny][nx] = 1
            heapq.heappush(q, (nd, ny, nx))
    print(distance)

bfs()