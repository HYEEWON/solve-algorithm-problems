from itertools import combinations
from itertools import product


def check(D, W, K):
    for j in range(W):
        col = False
        for i in range(D - K + 1):
            flag = True
            for k in range(i + 1, i + K, 1):
                if board[i][j] != board[k][j]:
                    flag = False
                    break
            if flag:
                col = True
                break
        if col == False:
            return False
    return True


T = int(input())
for t in range(1, T + 1, 1):
    ins = list(map(int, input().split()))
    D = ins[0];
    W = ins[1];
    K = ins[2];
    board = []
    for i in range(D):
        line = list(map(int, input().split()))
        board.append(line)

    for i in range(K + 1):
        chg = list(combinations([n for n in range(D)], i))
        ab = list(product([0, 1], repeat=i))
        tmp = [[0 for a in range(W)] for b in range(D)]
        for c in chg:
            for j in range(len(c)):
                tmp[c[j]] = board[c[j]]
            chk = False
            for idx in ab:
                for j in range(len(c)):
                    board[c[j]] = [idx[j] for _ in range(W)]
                chk = check(D, W, K)
                if chk == True:
                    print('#' + str(t) + ' ' + str(i))
                    break

            if chk == False:
                for j in range(len(c)):
                    board[c[j]] = tmp[c[j]]
            else:
                break
        if chk == True:
            break