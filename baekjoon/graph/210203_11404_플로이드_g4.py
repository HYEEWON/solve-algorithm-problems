import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
cost = [[10000001 for i in range(n)] for j in range(n)]

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    cost[a-1][b-1] = min(cost[a-1][b-1], c) # a에서 b로 가는 비용은 c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                cost[i][j] = 0
            elif (cost[i][k] + cost[k][j] < cost[i][j]):
                cost[i][j] = cost[i][k] + cost[k][j]

for i in range(n):
    for j in range(n):
        if cost[i][j] > 10000000:
            sys.stdout.write(str(0)+' ')
        else:
            sys.stdout.write(str(cost[i][j])+' ')
    sys.stdout.write('\n')