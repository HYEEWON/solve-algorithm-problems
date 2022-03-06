# Graph, Topological Sort, DFS, BFS

# 방향있는 그래프
# 탐색한 노드 수 == 수강 강의 수? 수강 가능 : 불가

from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0 for i in range(numCourses)]
        graph = defaultdict(list)
        q = deque()
        cnt = 0 # 방문한 노드 수

        for p in prerequisites:
            graph[p[1]].append(p[0])
            indegree[p[0]] += 1

        for node in range(numCourses):
            if indegree[node] == 0:
                q.append(node)

        while q:
            front = q.popleft()
            cnt += 1
            for node in graph[front]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    q.append(node)
        
        if cnt != numCourses:
            return False
        else:
            return True
