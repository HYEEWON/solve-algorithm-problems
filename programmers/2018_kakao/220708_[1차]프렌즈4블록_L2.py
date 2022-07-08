# Simulation

def check(y, x, board, visit):
    for j in range(y, y + 2):
        for i in range(x, x + 2):
            if board[y][x] == '-':
                return False
    if board[y][x] == board[y][x + 1] == board[y + 1][x] == board[y + 1][x + 1]:
        visit[y][x] = visit[y][x + 1] = visit[y + 1][x] = visit[y + 1][x + 1] = True
        return True
    return False

def change(board, visit):
    for x in range(len(board[0])):
        for y in range(len(board)):
            if not visit[y][x]:
                continue
            while visit[y][x]:
                for tmp_y in range(y, 0, -1):
                    board[tmp_y][x] = board[tmp_y - 1][x]
                    visit[tmp_y][x] = visit[tmp_y - 1][x]
                board[0][x], visit[0][x] = '-', False

def solution(m, n, board):
    answer = 0
    board = [list(b) for b in board]

    while True:
        visit = [[False for i in range(len(board[0]))] for j in range(len(board))]
        result = False
        for y in range(m - 1):
            for x in range(n - 1):
                tmp = check(y, x, board, visit)
                if tmp:
                    result = True
                if result == '-':
                    continue
        for v in visit:
            answer += v.count(True)
        if not result:
            break
        change(board, visit)
    return answer