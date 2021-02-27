import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().strip().split())

A = []
for n in range(N):
    A.append(list(map(int, sys.stdin.readline().strip().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
totals, counts = [0], [0]

def bfs(y, x, visit, n): # 세로, 가로
    global totals, counts
    flag = False
    dq = deque()
    dq.append([y, x]) # 세로, 가로, 전체 합, 칸 수

    total, cnt = 0, 0
    while dq:
        y, x = dq.popleft()
        total += A[y][x]
        cnt += 1

        for t in range(4):
            ny = y + dy[t]
            nx = x + dx[t]
            if ny<0 or nx<0 or ny>=N or nx>=N:
                continue
            if L <= abs(A[ny][nx]-A[y][x]) <= R and visit[ny][nx] == 0:
                visit[y][x] = visit[ny][nx] = n
                dq.append([ny, nx])
    if cnt > 1:
        flag = True
        totals.append(total)
        counts.append(cnt)
    return flag

def main():
    global totals, counts
    answer = 0
    while True:
        visit = [[0 for i in range(N)] for j in range(N)]
        totals, counts = [0], [0]
        n = 1
        for i in range(N):
            for j in range(N):
                if visit[i][j] == 0:
                    flag = bfs(i, j, visit, n)
                    if flag == True:
                        n += 1

        if len(counts) <= 1:
            sys.stdout.write(str(answer))
            return
        
        populations = [0 for i in range(n)]
        for i in range(1, n):
            populations[i] = totals[i] // counts[i]

        for p in range(N):
            for q in range(N):
                if visit[p][q] >0:
                    A[p][q] = populations[visit[p][q]]
        answer += 1

main()