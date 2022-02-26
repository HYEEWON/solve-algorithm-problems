'''
    1) BFS 사용
    2) 전체 좌표를 2배 -> ㄷ자일 경우, 잘못 판단되는 오류 제거
        - [예1] (3, 5) -> (3, 6)은 불가능하지만 가능하다고 판단 가능
'''

from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    # 좌표*2
    board = [[0 for j in range(1001)] for i in range(1001)]

    # 사각형의 테두리+내부를 1로 채움
    for x1, y1, x2, y2 in rectangle: # [좌측 하단 x, 좌측 하단 y, 우측 상단 x, 우측 상단 y]
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
    q.append((0, characterY, characterX))

    while q:
        cnt, y, x = q.popleft()
        board[y][x] = -1

        if board[itemY][itemX] < 0:
            return cnt // 2 # 좌표를 2배했으므로 2로 나눔

        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if board[y+dy][x+dx] > 0:
                q.append((cnt+1, y+dy, x+dx))
