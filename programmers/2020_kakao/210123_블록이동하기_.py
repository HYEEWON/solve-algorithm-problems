from collections import deque
def solution(board):
    N = len(board)
    visit = [[[0, 0, 0, 0] for i in range(N)] for j in range(N)]
    dq = deque()
    dq.append([[(0, 0), (0, 1)], '-', 0]) #위치, 방향, 이동 수
    visit[0][0][0], visit[0][1][1] = 1, 1
    
    while dq:
        pos, drt, cnt = dq.popleft()

        if drt == '-':





board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))
