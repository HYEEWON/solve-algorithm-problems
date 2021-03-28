import sys
from collections import defaultdict

N = int(sys.stdin.readline())
nodes = list(map(int, sys.stdin.readline().strip().split()))
target = int(sys.stdin.readline())

tree = defaultdict(list)
for i in range(N):
    tree[nodes[i]].append(i)

def dfs(node):
    if node not in tree.keys():
        return
    for n in tree[node]:
        if visit[n] == 1:
            visit[n] = 0
            dfs(n)
    tree.pop(node)

visit = [1] * N
for key in tree.keys():
    if target in tree[key]:
        visit[target] = 0
        tree[key].remove(target)
        dfs(target)
        break

answer = 0
for node in range(N):
    if visit[node] > 0 and (node not in tree.keys() or tree[node] == []):
        answer += 1
print(answer)

'''
class Node:
    def __init__(self, parent, data):
        self.parent = parent
        self.data = data

N = int(sys.stdin.readline())
nodes = list(map(int, sys.stdin.readline().strip().split()))
target = int(sys.stdin.readline())

tree = {}
parents = [0] * N
for i in range(N):
    if nodes[i] != -1:
        parents[nodes[i]] += 1
    tree[i] = Node(nodes[i], i)

keys = list(tree.keys())
flag = [1] * N
for key in keys[:]:
    if tree[key].data == target or tree[key].parent == target or flag[tree[key].parent] == 0:
        print(key, tree[key].parent, tree[key].data)
        flag[key] = 0
        parents[tree[key].parent] -= 1

print(flag)
print(parents)
answer = 0
for i in range(N):
    if flag[i] == 1 and parents[i] == 0:
        answer += 1

sys.stdout.write(str(answer))
'''