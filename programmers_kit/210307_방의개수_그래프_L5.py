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

    for arrow in arrows:
        ny = y + dy[arrow]
        nx = x + dx[arrow]

        cnt[(y, x)] = 0
        cnt[(ny, nx)] = 0
        graph[(y, x, ny, nx)] = 0
        graph[(ny, nx, y, x)] = 0
        q.append([ny, nx])
        y, x = ny, nx

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