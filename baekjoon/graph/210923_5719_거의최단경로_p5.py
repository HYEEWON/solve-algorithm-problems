# 다익스트라
# 거의 최단 경로: 최단 경로에 포함되지 않는 도로로만 이루어진 경로 중 가장 짧은 것

import sys, heapq
from collections import deque

def dijkstra(start, end):
    dist[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))

    while len(pq) > 0:
        cur_cost, cur_node = heapq.heappop(pq)
        if cur_node == end:
            continue
        if cur_cost > dist[cur_node]:
            continue

        for next in range(0, N):
            if graph[cur_node][next] == 0:
                continue
            elif dist[next] > dist[cur_node] + graph[cur_node][next]:
                dist[next] = dist[cur_node] + graph[cur_node][next]
                heapq.heappush(pq, (dist[next], next))

def bfs(end, N):
    q = deque()
    isVisit = [False for i in range(N)]

    q.append(end)
    while q:
        node = q.popleft()
        if isVisit[node]:
            continue
        isVisit[node] = True

        for before in range(0, N):
            if graph[before][node] == 0:
                continue
            elif dist[node] == dist[before] + graph[before][node]:
                graph[before][node] = 0
                q.append(before)

N, M = map(int, sys.stdin.readline().strip().split())

while N!=0 and M!=0:
    S, D = map(int, sys.stdin.readline().strip().split())

    graph = [[0 for i in range(N)] for j in range(N)]
    for i in range(M):
        U, V, P = map(int, sys.stdin.readline().strip().split())
        graph[U][V] = P

    dist = [sys.maxsize for i in range(N)]
    # 최단 경로 찾기
    dijkstra(S, D)

    # 최단 경로 삭제
    bfs(D, N)

    dist = [sys.maxsize for i in range(N)]
    # 거의 최단 경로 찾기
    dijkstra(S, D)

    if dist[D] == sys.maxsize:
        sys.stdout.write(str(-1) + "\n")
    else:
        sys.stdout.write(str(dist[D]) + "\n")
    N, M = map(int, sys.stdin.readline().strip().split())
