# 다익스트라 알고리즘 사용
# 우선순위 큐로 heapq 사용
# 입출력은 sys를 사용해야 시간 초가가 되지 않음

from collections import defaultdict
import sys, heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

buses = defaultdict(list)

class Bus:
    def __init__(self, end, cost):
        self.end = end
        self.cost = cost


for i in range(M):
    start, end, cost = map(int, sys.stdin.readline().strip().split())
    buses[start].append(Bus(end, cost))

startCity, endCity = map(int, sys.stdin.readline().strip().split())

pq = []
dist = [sys.maxsize for i in range(N+1)]
isVisit = [False for i in range(N+1)]

dist[startCity] = 0

heapq.heappush(pq, (0, startCity))

while pq:
    cost, cur = heapq.heappop(pq)
    
    if isVisit[cur]:
        continue
    isVisit[cur] = True

    for bus in buses[cur]:
        if (dist[bus.end] > dist[cur] + bus.cost):
            dist[bus.end] = dist[cur] + bus.cost
            heapq.heappush(pq, (dist[bus.end], bus.end))

sys.stdout.write(str(dist[endCity]))