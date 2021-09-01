# BFS 사용
# visit 배열을 2차원으로 하여 로봇이 가로, 세로일 경우를 저장
# 가로일 경우: 왼쪽 기준, 세로일 경우: 오른쪽 기준

from collections import deque

def solution(board):
    N = len(board)
    visit = [[[0, 0] for i in range(N)] for j in range(N)]
    dq = deque()
    dq.append([0, 0, '-', 0]) #위치, 방향, 이동 수
    visit[0][0][0] = 1
    
    while dq:
        y, x, drt, cnt = dq.popleft()
        if (y == N-1 and x == N-2 and drt == '-') or (y == N-2 and x == N-1 and drt == '|'):
            return cnt

        if drt == '-': # 로봇이 가로인 경우
            if x > 0: # 왼쪽 이동
                if board[y][x-1] == 0 and visit[y][x-1][0] == 0:
                    visit[y][x-1][0] = 1
                    dq.append([y, x - 1, '-', cnt + 1])
            if x < N-2: # 오른쪽 이동
                if board[y][x+2] == 0 and visit[y][x+1][0] == 0:
                    visit[y][x+1][0] = 1
                    dq.append([y, x + 1, '-', cnt + 1])
            if y > 0:
                if board[y-1][x] == 0 and board[y-1][x+1] == 0 and visit[y-1][x][0] == 0: # 위쪽 이동
                    visit[y-1][x][0] = 1
                    dq.append([y - 1, x, '-', cnt + 1])
                if board[y-1][x] == 0 and board[y-1][x+1] == 0 and visit[y-1][x][1] == 0:
                    visit[y-1][x][1] = 1
                    dq.append([y-1, x, '|', cnt + 1])
                if board[y-1][x] == 0 and board[y-1][x+1] == 0 and visit[y-1][x+1][1] == 0:
                    visit[y-1][x+1][1] = 1
                    dq.append([y-1, x+1, '|', cnt + 1])
            if y < N-1:
                if board[y+1][x] == 0 and board[y+1][x+1] == 0 and visit[y+1][x][0] == 0: # 아래쪽 이동
                    visit[y+1][x][0] = 1
                    dq.append([y+1, x, '-', cnt + 1])
                if board[y+1][x] == 0 and board[y+1][x+1] == 0 and visit[y][x][1] == 0:
                    visit[y][x][1] = 1
                    dq.append([y, x, '|', cnt + 1])
                if board[y+1][x] == 0 and board[y+1][x+1] == 0 and visit[y][x+1][1] == 0:
                    visit[y][x+1][1] = 1
                    dq.append([y, x+1, '|', cnt + 1])
        else: # 로봇이 세로인 경우
            if x > 0:
                if board[y][x-1] == 0 and board[y+1][x-1] == 0 and visit[y][x-1][1] == 0: # 왼쪽 이동
                    visit[y][x-1][1] = 1
                    dq.append([y, x-1, '|', cnt + 1])
                if board[y][x-1] == 0 and board[y+1][x-1] == 0 and visit[y][x-1][0] == 0:
                    visit[y][x-1][0] = 1
                    dq.append([y, x-1, '-', cnt + 1])
                if board[y+1][x-1] == 0 and board[y][x-1] == 0 and visit[y+1][x-1][0] == 0:
                    visit[y+1][x-1][0] = 1
                    dq.append([y+1, x-1, '-', cnt + 1])
            if x < N-1:
                if board[y][x+1] == 0 and board[y+1][x+1] == 0 and visit[y][x+1][1] == 0: # 오른쪽 이동
                    visit[y][x+1][1] = 1
                    dq.append([y, x+1, '|', cnt + 1])
                if board[y][x+1] == 0 and board[y+1][x+1] == 0 and visit[y][x][0] == 0:
                    visit[y][x][0] = 1
                    dq.append([y, x, '-', cnt + 1])
                if board[y+1][x+1] == 0 and board[y][x+1] == 0 and visit[y+1][x][0] == 0:
                    visit[y+1][x][0] = 1
                    dq.append([y+1, x, '-', cnt + 1])
            if y > 0:
                if board[y-1][x] == 0 and visit[y-1][x][1] == 0:
                    visit[y-1][x][1] = 1
                    dq.append([y - 1, x, '|', cnt + 1])
            if y < N-2:
                if board[y+2][x] == 0 and visit[y+1][x][1] == 0:
                    visit[y+1][x][1] = 1
                    dq.append([y+1, x, '|', cnt + 1])


board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))
