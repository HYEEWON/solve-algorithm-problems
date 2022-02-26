from collections import deque, defaultdict
import sys

graph = defaultdict(list)

def bfs(x, w, visit):
    visit[x] = 1

    q = deque()
    q.append(x)
    cnt = 1

    while q:
        n = q.popleft()

        for node in graph[n]:
            if [node, n] == w or [n, node] == w:
                continue
            if visit[node] == 1:
                continue
            visit[node] = 1
            cnt += 1
            q.append(node)

    return cnt

def solution(n, wires):
    answer = sys.maxsize

    for w in wires:
        graph[w[0]].append(w[1])
        graph[w[1]].append(w[0])

    for i in range(len(wires)):
        visit = [0 for i in range(n+1)]
        cnt = []
        for x in range(1, n+1):
            if visit[x] == 0:
                cnt.append(bfs(x, wires[i], visit))
                print(visit)
                print(cnt)
        answer = min(answer, abs(cnt[0]-cnt[1]))
    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
#print(solution(4, [[1,2],[2,3],[3,4]]))