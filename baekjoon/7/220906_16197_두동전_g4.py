# 백트랙킹

# 주의 사항
# visit에 저장 -> back_tracking() 수행 -> visit에서 삭제
# 삭제를 하지 않아서 오류 찾는데 오래 걸림

# 참고
# visit[py1][px1][py2][px2]로 할 수도 있음


import sys

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
board = []
position = []
answer = sys.maxsize
visit = set()

N, M = map(int, sys.stdin.readline().strip().split())

board.append(['.' for i in range(M + 2)])
for i in range(1, N + 1):
    board.append(['.'] + list(sys.stdin.readline().strip()) + ['.'])
    for j in range(1, M + 1):
        if board[i][j] == 'o':
            position.append((i, j))
            board[i][j] = '.'
board.append(['.' for i in range(M + 2)])

visit = set()
visit.add((position[0], position[1]))


def back_tracking(y1, x1, y2, x2, cnt):
    global answer
    if cnt > 10:
        return

    for i in range(4):
        if board[y1 + dy[i]][x1 + dx[i]] != '#':
            ny1, nx1 = y1 + dy[i], x1 + dx[i]
        else:
            ny1, nx1 = y1, x1
        if board[y2 + dy[i]][x2 + dx[i]] != '#':
            ny2, nx2 = y2 + dy[i], x2 + dx[i]
        else:
            ny2, nx2 = y2, x2

        if not 0<=ny1<N+2 or not 0<=nx1<M+2 or not 0<=ny2<N+2 or not 0<=nx2<M+2:
            continue
        if ((ny1, nx1), (ny2, nx2)) in visit:
            continue
        if ny1 == ny2 and nx1 == nx2:
            visit.add(((ny1, nx1), (ny2, nx2)))
            continue

        np1, np2 = is_inboard(ny1, nx1), is_inboard(ny2, nx2)
        if np1 and np2:
            visit.add(((ny1, nx1), (ny2, nx2)))
            back_tracking(ny1, nx1, ny2, nx2, cnt + 1)
            visit.remove(((ny1, nx1), (ny2, nx2)))
        elif (not np1 and np2) or (np1 and not np2):
            answer = min(answer, cnt + 1)


def is_inboard(y, x):
    global N, M
    if 0 < y <= N and 0 < x <= M:
        return True
    return False


back_tracking(position[0][0], position[0][1], position[1][0], position[1][1], 0)
if answer > 10:
    answer = -1
sys.stdout.write(str(answer))