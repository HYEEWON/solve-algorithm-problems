from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(y, x, visit, place):
    dq = deque()
    dq.append([y, x, 0])

    cnt = 0
    while dq:
        
        y, x, dist = dq.popleft()
        if dist >= 2:
            break
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if (ny<0 or ny>=5 or nx<0 or nx>=5) or visit[ny][nx] == 1:
                continue

            if place[ny][nx] == 'P':             
                return 0
            elif place[ny][nx] == 'O':
                dq.append([ny, nx, dist+1])             
        cnt += 1        
    return 1

def solution(places):
    answer = []
    for idx in range(len(places)):
        visit = [[0 for k in range(5)] for j in range(5)]
        place = places[idx]
        result = -1
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P' and visit[i][j] == 0:
                    visit[i][j] = 1
                    result = bfs(i, j, visit, place)
                    if result == 0:
                        answer.append(0)
                        break
            if result == 0:
                break
            if i == 4:
                answer.append(1)
    return answer