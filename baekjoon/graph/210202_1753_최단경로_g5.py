// 다익스트라 알고리즘
import sys, heapq
from collections import defaultdict

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline().strip())

dist = [float('inf')] * (V+1)
visit = [False] * (V+1)
pq = [] # 우선 순위 큐
graph = [[] for _ in range(V+1)]

for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

def dijkstra(start):
    heapq.heappush(pq, (0, start))
    dist[start] = 0 #시작점 ~ 시작점의 거리: 0

    while pq:
        cost, now = heapq.heappop(pq)
        
        if visit[now] == True: 
            continue
        visit[now] = True

        for nextNode in graph[now]:
            if dist[nextNode[0]] > nextNode[1] + dist[now]:
                dist[nextNode[0]] = nextNode[1] + dist[now]
                heapq.heappush(pq, (dist[nextNode[0]], nextNode[0]))

dijkstra(K)

for i in range(1, len(dist)):
    if (dist[i] == float('inf')):
        sys.stdout.write("INF\n")
    else:
        sys.stdout.write(str(dist[i])+"\n")