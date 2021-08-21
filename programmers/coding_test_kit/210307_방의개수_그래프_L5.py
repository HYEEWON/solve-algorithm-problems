from collections import deque, defaultdict

dy = [1, 1, 0, -1, -1, -1, 0, 1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

def solution(arrows):
    answer = 0
    graph = defaultdict(int)
    cnt = defaultdict(int)

    x, y = 0, 0
    q = deque()
    q.append([y, x])

    # 1번 이동할 때, 2번씩 이동
    for i in arrows:
        for j in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            cnt[(ny, nx)] = 0
            graph[(y, x, ny, nx)] = 0
            graph[(ny, nx, y, x)] = 0
            q.append([ny, nx])
            x, y = nx, ny

    y, x = q.popleft()
    cnt[(y, x)] = 1

    while q:
        ny, nx = q.popleft()    
        if cnt[(ny, nx)] > 0:
            if graph[(y, x, ny, nx)] == 0:
                answer += 1
                graph[(y, x, ny, nx)] += 1
                graph[(ny, nx, y, x)] += 1
        else:
            cnt[(ny, nx)] += 1
            graph[(y, x, ny, nx)] += 1
            graph[(ny, nx, y, x)] += 1
        y, x = ny, nx    
    return answer

arrows = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]
print(solution(arrows))