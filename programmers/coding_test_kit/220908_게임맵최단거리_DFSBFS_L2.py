# bfs 

from collections import deque

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def solution(maps):
    return bfs(0, 0, maps)
    
def bfs(y, x, maps):
    visit = [[False for i in range(len(maps[0]))] for j in range(len(maps))]
    visit[y][x] = True
    
    q = deque()
    q.append((y, x, 1))
    
    while q:
        y, x, cnt = q.popleft()
        if y == len(maps)-1 and x == len(maps[0])-1:
            return cnt
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            
            if not 0<=ny<len(maps) or not 0<=nx<len(maps[0]):
                continue
            if maps[ny][nx] == 0 or visit[ny][nx]:
                continue

            visit[ny][nx] = True
            q.append((ny, nx, cnt+1))
    return -1
