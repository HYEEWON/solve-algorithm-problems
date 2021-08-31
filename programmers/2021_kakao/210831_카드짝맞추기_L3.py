# 참고한 풀이
# 모든 경우의 수를 탐색 + BFS

from collections import deque, defaultdict
import math

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

Board = []
cards = defaultdict(list)
all_removed = 1
min_cnt = math.inf

def bfs(removed, start, end):
    visit = [[False for i in range(4)] for j in range(4)]
    q = deque()
    q.append(start) # y, x, cost

    while q:
        y, x, cnt = q.popleft()
        if y == end[0] and x == end[1]:
            return cnt

        # 이동
        for i in range(4):
            # 일반 방향키 이동
            ny = y + dy[i]
            nx = x + dx[i]

            if not 0 <= nx < 4 or not 0 <= ny < 4:
                continue
            if not visit[ny][nx]:
                visit[ny][nx] = True
                q.append((ny, nx, cnt + 1))

            # 컨트롤 이동 (최대 2번 더 이동 가능)
            for j in range(2):
                if (removed & 1 << Board[ny][nx]) == 0: # 카드가 존재하는 경우
                    break
                if not 0 <= (nx + dx[i]) < 4 or not 0 <= (ny + dy[i]) < 4:
                    break
                ny += dy[i]
                nx += dx[i]
                
            if not visit[ny][nx]:
                visit[ny][nx] = True
                q.append((ny, nx, cnt + 1))
    return math.inf

# 지금까지의 이동 수, 삭제 여부, 현재 커서의 위치
def permutation(cnt, removed, pos): 
    global all_removed, min_cnt

    if cnt >= min_cnt:
        return

    if removed == all_removed:
        min_cnt = min(min_cnt, cnt)
        return
    
    for num, card in cards.items():
        if removed & 1 << num: # 삭제된 카드일경우
            continue
        # (현재 위치 -> 카드1) + (카드1 -> 카드2) + 엔터 2번
        one = bfs(removed, pos, card[0]) + bfs(removed, card[0], card[1]) + 2
        two = bfs(removed, pos, card[1]) + bfs(removed, card[1], card[0]) + 2

        permutation(cnt + one, removed | 1 << num, card[1])
        permutation(cnt + two, removed | 1 << num, card[0])
        
def solution(board, r, c):
    global Board, min_cnt, all_removed
    Board = board

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] != 0:
                all_removed |= 1<<board[row][col]
                cards[board[row][col]].append((row, col, 0))

    permutation(0, 1, (r, c, 0))

    return min_cnt

print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))


'''def bfs(removed, start, end):
    visit = [[False for i in range(4)] for j in range(4)]
    q = deque()
    q.append((start[0], start[1], 0)) # y, x, cost
    visit[start[0]][start[1]][0] = True
    visit[start[0]][start[1]][1] = True

    while q:
        y, x, cnt = q.popleft()
        if y == end[0] and x == end[1]:
            return cnt

        # 일반 방향키 이동
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if (not 0<=nx<4 or not 0<=ny<4) or visit[ny][nx][0] == True:
                continue
            visit[ny][nx][0] = True
            q.append((ny, nx, cnt+1))

        #  컨트롤 + 방향키 이동
        for i in range(4):
            for j in range(3):
            #while True:
                y += dy[i]
                x += dx[i]
                if (not 0 <= x < 4 or not 0 <= y < 4) or visit[y][x][0] == True:
                    continue

                if board[y][x] != 0:
                    visit[y][x][1] = True
                    q.append((y, x, cnt + 1))
                    break
                if (i == 0 and x == 3) or (i == 1 and x == 0) or (i == 2 and y == 3) or (i == 3 and y == 0):
                    visit[y][x][1] = True
                    q.append((y, x, cnt + 1))
                    break
'''