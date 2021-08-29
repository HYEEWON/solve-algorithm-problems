import sys

def find_path(start, end):
    if route[start][end] == 0:
        return []

    stop_over = route[start][end]
    return find_path(start, stop_over) + [str(stop_over)] + find_path(stop_over, end)


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

# 최단 경로의 비용 저장
costs = [[sys.maxsize for i in range(N+1)] for j in range(N+1)]

# 최단 경로 저장
# route[i][j]: j에 도달하기 위해 경유하는 노드 저장 (j 직전에 경유하는 노드)
route = [[0 for i in range(N+1)] for j in range(N+1)]

for i in range(M):
    start, end, cost = map(int, sys.stdin.readline().strip().split())
    costs[start][end] = min(costs[start][end], cost) # start에서 end로 가는 비용은 cost

for k in range(1, N+1):
    for s in range(1, N+1):
        for e in range(1, N+1):
            if s == e:
                costs[s][e] = 0
            else:
                # costs[s][e] = min(costs[s][e], costs[s][k] + costs[k][e])
                if costs[s][e] > costs[s][k] + costs[k][e]:
                    costs[s][e] = costs[s][k] + costs[k][e]
                    route[s][e] = k

for s in range(1, N+1):
    for e in range(1, N+1):
        if costs[s][e] >= sys.maxsize:
            sys.stdout.write(str(0)+' ')
        else:
            sys.stdout.write(str(costs[s][e]) + ' ')
    sys.stdout.write('\n')

for s in range(1, N+1):
    for e in range(1, N+1):
        if costs[s][e] in [0, sys.maxsize]:
            sys.stdout.write('0 \n')
        else:
            path = [str(s)] + find_path(s, e) + [str(e)]
            sys.stdout.write(str(len(path)) + ' ' + ' '.join(path) + '\n')
