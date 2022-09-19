from collections import defaultdict, deque
import sys, heapq

# 방법1
# 다익스트라 활용

answer = [0, sys.maxsize]
graph = defaultdict(list)

def solution(n, paths, gates, summits):
    global answer, graph

    for path in paths:
        graph[path[0]].append((path[1], path[2]))
        graph[path[1]].append((path[0], path[2]))

    gates, summits = set(gates), set(summits)
    dijkstra(n, gates, summits)
    return answer

def dijkstra(n, gates, summits):
    global answer, graph

    intensity = [sys.maxsize for i in range(n + 1)]
    pq = []  # 우선순위 큐

    for node in gates:
        heapq.heappush(pq, (0, node))  # (intensity, node 번호)
        intensity[node] = 0

    while pq:
        cur_intensity, now = heapq.heappop(pq)
        if cur_intensity > answer[1]:
            continue

        if now in summits:
            if answer[1] > cur_intensity or (answer[1] == cur_intensity and answer[0] > now):
                answer = [now, cur_intensity]
            continue

        for next, cost in graph[now]:
            new_intensity = max(cur_intensity, cost)
            if new_intensity < intensity[next]:
                intensity[next] = new_intensity
                heapq.heappush(pq, (new_intensity, next))


# 방법2
# 이분탐색 + bfs
# 이분탐색으로 최소 intensity를 구하고 bfs로 산봉우리를 구함

graph = defaultdict(list)

def solution(n, paths, gates, summits):
    global graph
    answer = [-1, -1]
    for path in paths:
        graph[path[0]].append((path[1], path[2]))
        graph[path[1]].append((path[0], path[2]))

    gates, summits = set(gates), set(sorted(summits))
    start, end = 1, 10000000
    # # 이진탐색으로 가장 작은 intensity를 찾음
    while start <= end:
        mid = (start + end) // 2
        ret = bfs(n, mid, gates, summits)
        if ret == -1:
            start = mid + 1
        else:
            end = mid - 1
            answer = [ret, mid]
    return answer


def bfs(n, target, gates, summits):
    global graph
    ret = sys.maxsize
    q = deque()
    visit = [False for i in range(n + 1)]

    for start in gates: # 미리 출발점 방문
        visit[start] = True
        q.append(start)

    while q:
        now = q.popleft()
        for next, cost in graph[now]:
            if cost > target or visit[next]: continue
            if next in summits:
                if ret > next:
                    ret = next
                continue
            visit[next] = True
            q.append(next)
    return -1 if ret == sys.maxsize else ret
