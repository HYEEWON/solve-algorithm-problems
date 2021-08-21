from collections import defaultdict, deque

def solution(n, edge):
    answer = 0
    graph = defaultdict(list)
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    distance = [-1] * (n+1)
    q = deque()
    q.append([1, 0])
    distance[1] = 0
    
    while q:
        node, dist = q.popleft()
        for n in graph[node]:
            if distance[n] == -1:
                distance[n] = dist+1
                q.append([n, dist+1])

    answer = distance.count(max(distance))
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))