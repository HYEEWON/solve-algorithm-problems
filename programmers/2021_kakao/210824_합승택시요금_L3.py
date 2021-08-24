# 다익스트라 알고리즘 사용 (플로이드 웨셸도 가능)
# 최소 값을 구하는 것은 for loop 사용
# 정확성과 효율성 모두 중요

import sys, heapq

def dijkstra(n, s, e, nodes):    
    pq = []
    dist = [sys.maxsize for i in range(n+1)]
    isVisit = [False for i in range(n+1)]

    heapq.heappush(pq, (0, s))
    dist[s] = 0

    while pq:
        cost, cur = heapq.heappop(pq)

        if isVisit[cur]:
            continue
        isVisit[cur] = True

        for node in nodes[cur]:
            if dist[node[0]] > dist[cur] + node[1]:
                dist[node[0]] = dist[cur] + node[1]
                heapq.heappush(pq, (dist[node[0]], node[0]))

    return dist[e]

def solution(n, s, a, b, fares):
    answer = sys.maxsize
    nodes = [[] for i in range(n+1)]
    for fare in fares:
        nodes[fare[0]].append([fare[1], fare[2]])
        nodes[fare[1]].append([fare[0], fare[2]])
    
    for i in range(1, n+1):
        answer = min(answer, dijkstra(n, s, i, nodes) + dijkstra(n, i, a, nodes) + dijkstra(n, i, b, nodes))
    return answer

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))