# 최소 신장 트리
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
parent = {}

def find(x):
    if parent[x] == x:
        return x
    y = find(parent[x])
    parent[x] = y
    return y

def union(x, y):
    x = find(x)
    y = find(y)
    if (x != y):
        parent[y] = x

tree = []
while True:
    try:
        a, b, c = map(int, sys.stdin.readline().split())
        tree.append([[a, b], c])
        parent[a] = a
        parent[b] = b
    except:
        break

tree = sorted(tree, key = lambda x: x[1])
minCost = 0

for edge in tree:
    node, weight = edge
    node1, node2 = node
    # 비용이 적은 노드부터 연결해 최소 비용 계산 가능
    if find(node1) != find(node2):
        union(node1, node2)
        minCost += weight

print(minCost)