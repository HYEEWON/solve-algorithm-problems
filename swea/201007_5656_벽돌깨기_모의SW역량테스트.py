from itertools import product
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def breaks(y, x):
    global tmp
    if tmp[y][x] > 0:
        t = tmp[y][x]
        tmp[y][x] = 0

        for it in range(1, t):
            for i in range(4):
                nx = x + dx[i] * it
                ny = y + dy[i] * it
                if 0 <= nx < W and 0 <= ny < H and tmp[ny][nx] > 0:
                    breaks(ny, nx)


T = int(input())
for t in range(1, T + 1):
    inp = list(map(int, input().split()))
    N = inp[0];
    W = inp[1];
    H = inp[2];
    board = []
    C = list(product([i for i in range(W)], repeat=N))

    for h in range(H):
        line = list(map(int, input().split()))
        board.append(line)

    cnt = H * W
    for c in C:
        tmp = copy.deepcopy(board)
        for x in c:
            for y in range(H):
                if tmp[y][x] > 0:
                    breaks(y, x)

                    for idx in range(W):
                        s = []
                        for idy in range(H):
                            if tmp[idy][idx] > 0:
                                s.append(tmp[idy][idx])
                        for p in range(H - len(s)):
                            tmp[p][idx] = 0
                        for p in range(H - len(s), H):
                            tmp[p][idx] = s[p - H + len(s)]
                    break

        new_cnt = 0
        for i in range(H - 1, -1, -1):  # 카운트
            if tmp[i].count(0) >= W:
                break
            for j in range(W):
                if tmp[i][j] > 0:
                    new_cnt += 1
        cnt = min(cnt, new_cnt)
        if cnt == 0:
            break
    print('#' + str(t) + ' ' + str(cnt))