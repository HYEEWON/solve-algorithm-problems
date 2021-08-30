import sys

class Edge:
    def __init__(self, start, end, cost):
        self.start = start
        self.end = end
        self.cost = cost

def find(x):
    if parents[x] == x:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]

# 정점의 수 (1~V), 간선의 수
V, E = map(int, sys.stdin.readline().strip().split())
edges = []
parents = [i for i in range(V+1)]

for e in range(E):
    A, B, C = map(int, sys.stdin.readline().strip().split())
    edges.append(Edge(A, B, C))

# 가중치를 기준으로 오름차순 정렬
edges = sorted(edges, key=lambda x: x.cost)

sum_cost = 0
for edge in edges:
    s = find(edge.start)
    e = find(edge.end)
    
    # 루트가 같다면 MST가 아님
    if s == e:
        continue

    # 루트가 다르다면 합침
    parents[e] = s
    sum_cost += edge.cost

sys.stdout.write(str(sum_cost))
