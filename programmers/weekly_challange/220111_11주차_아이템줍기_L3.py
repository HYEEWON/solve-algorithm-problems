'''
    1) BFS 사용
    2) 전체 좌표를 2배 -> ㄷ자일 경우, 잘못 판단되는 오류 제거
        - [예1] (3, 5) -> (3, 6)은 불가능하지만 가능하다고 판단 가능
'''

from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    # 좌표*2
    board = [[0 for j in range(101)] for i in range(101)]
    visit = [[False for j in range(101)] for i in range(101)]
    answer = 0

    # 사각형의 테두리+내부를 1로 채움
    for x1, y1, x2, y2 in rectangle:
        for i in range(2*y1, 2*y2+1):
            for j in range(2*x1, 2*x2+1):
                board[i][j] = 1

    # 사각형 내부를 0으로 채움
    for x1, y1, x2, y2 in rectangle:
        for i in range(2*y1+1, 2*y2):
            for j in range(2*x1+1, 2*x2):
                board[i][j] = 0

    characterX, characterY, itemX, itemY = 2*characterX, 2*characterY, 2*itemX, 2*itemY

    # BFS
    q = deque()
    q.append((0, characterX, characterY))

    while q:
        cnt, x, y = q.popleft()
        visit[y][x] = True

        if x == itemX and y == itemY:
            answer = cnt // 2

        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if visit[y+dy][x+dx]:
                continue

            if board[y+dy][x+dx] > 0:
                q.append((cnt+1, x+dx, y+dy))

    # 좌표를 2배했으므로 2로 나눔
    return answer


print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))

