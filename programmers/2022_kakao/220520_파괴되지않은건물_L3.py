# 누적 합

def solution(board, skill):
    answer = 0
    sum_d = [[0 for i in range(len(board[0])+1)] for j in range(len(board)+1)]

    for t, r1, c1, r2, c2, degree in skill:
        if t == 1:
            sum_d[r1][c1] -= degree
            sum_d[r1][c2 + 1] += degree
            sum_d[r2 + 1][c1] += degree
            sum_d[r2 + 1][c2 + 1] -= degree
        else:
            sum_d[r1][c1] += degree
            sum_d[r1][c2 + 1] -= degree
            sum_d[r2 + 1][c1] -= degree
            sum_d[r2 + 1][c2 + 1] += degree

    # 행 방향
    for i in range(len(board)):
        for j in range(len(board[0])):
            sum_d[i][j+1] += sum_d[i][j]

    # 열 방향
    for i in range(len(board)):
        for j in range(len(board[0])):
            sum_d[i+1][j] += sum_d[i][j]

    # 기존 배열에 더함
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += sum_d[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer
