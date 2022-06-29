def lotate(key):
    return list(map(list, zip(*key[::-1])))


def solution(key, lock):
    answer = True
    M, N = len(key), len(lock)
    new_lock = [[-2] * (2 * M + N - 2) for i in range(2 * M + N - 2)]

    for y in range(M - 1, M - 1 + N):
        for x in range(M - 1, M - 1 + N):
            new_lock[y][x] = lock[y - M + 1][x - M + 1]

    for i in range(4):
        for h in range(M + N - 1):
            for w in range(M + N - 1):
                answer = True
                for y in range(M - 1, M - 1 + N):
                    for x in range(M - 1, M - 1 + N):
                        if h <= y < h + M and w <= x < w + M:
                            if key[y - h][x - w] + new_lock[y][x] in [0, 2]:
                                answer = False
                                break
                        else:
                            if new_lock[y][x] != 1:
                                answer = False
                                break
                    if not answer:
                        break
                    if answer and y == M - 2 + N:
                        return answer
        key = lotate(key)
    return answer

