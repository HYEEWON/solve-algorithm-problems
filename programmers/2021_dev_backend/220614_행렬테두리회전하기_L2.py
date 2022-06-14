# 구현

def move(board, min_v, x, y, x1, y1, x2, y2):
    if x == x1 and y != y2:
        board[x][y+1] = board[x][y]
    elif y == y2 and x != x2:
        board[x+1][y] = board[x][y]
    elif x == x2 and y != y1:
        board[x][y-1] = board[x][y]
    else:
        board[x-1][y] = board[x][y]
    return min(min_v, board[x][y])

def solution(rows, columns, queries):
    answer = []
    board = [[i * columns + j +1 for j in range(columns)] for i in range(rows)]

    for query in queries:
        x1, y1, x2, y2 = query[0]-1, query[1]-1, query[2]-1, query[3]-1
        tmp, min_v = board[x1][y1], 10001
        for x in range(x1+1, x2+1):
            min_v = move(board, min_v, x, y1, x1, y1, x2, y2)
        for y in range(y1+1, y2+1):
            min_v = move(board, min_v, x2, y, x1, y1, x2, y2)
        for x in range(x2-1, x1-1, -1):
            min_v = move(board, min_v, x, y2, x1, y1, x2, y2)
        for y in range(y2, y1, -1):
            min_v = move(board, min_v, x1, y, x1, y1, x2, y2)
        board[x1][y1+1] = tmp
        answer.append(min(min_v, tmp))

    return answer