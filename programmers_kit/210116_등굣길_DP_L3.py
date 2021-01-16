from collections import deque, defaultdict

def solution(m, n, puddles):
    map = [[0 for i in range(m+1)] for j in range(n+1)]
    for p in puddles:
        map[p[1]][p[0]] = -1
    for i in range(1, n+1):
        if map[i][1] == -1:
            break
        map[i][1] = 1
    for j in range(1, m+1):
        if map[1][j] == -1:
            break
        map[1][j] = 1
        
    for i in range(2, n+1):
        for j in range(2, m+1):
            if map[i][j] == -1 or (map[i-1][j] < 0 and map[i][j-1] < 0):
                continue
            if map[i-1][j] == -1:
                map[i][j] = map[i][j-1]
            elif map[i][j-1] == -1:
                map[i][j] = map[i-1][j]
            else:
                map[i][j] = map[i][j-1] + map[i-1][j]
            map[i][j] %= 1000000007
    return map[n][m]

from collections import deque, defaultdict

def solution2(m, n, puddles):
    map = [[0 for i in range(m+1)] for j in range(n+1)]
    for p in puddles:
        map[p[1]][p[0]] = -1
    map[1][1] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == j == 1:
                continue
            if map[i][j] == -1:
                map[i][j] = 0
            else:
                map[i][j] = (map[i][j-1] + map[i-1][j]) % 1000000007
    return map[n][m]