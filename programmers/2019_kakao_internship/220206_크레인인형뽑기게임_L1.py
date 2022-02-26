from collections import deque

def solution(board, moves):
    answer = 0
    dolls = [deque() for i in range(len(board))]
    basket = deque()

    for x in range(len(board)):
        for y in range(len(board)):
            if board[y][x] != 0:
                dolls[x].append(board[y][x])

    for pos in moves:
        if len(dolls[pos-1]) == 0:
            continue
        doll = dolls[pos-1].popleft()

        if basket and basket[-1] == doll:
            basket.pop()
            answer += 2
        else:
            basket.append(doll)

    return answer
