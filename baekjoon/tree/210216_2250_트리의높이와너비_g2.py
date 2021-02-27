import sys
from collections import defaultdict

N = int(sys.stdin.readline().strip())

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

tree = {}
parents = [0 for i in range(N+1)]
for i in range(1, N+1):
    node, left, right = map(int, sys.stdin.readline().strip().split())
    tree[node] = Node(node, left, right)
    if left != -1:
        parents[left] = node
    if right != -1:
        parents[right] = node

# 중위순회는 왼 -> 부모 -> 오른 순서로 방문하여 방문 순서가 곧 좌표
point = 1
nodes = defaultdict(list)

def inOrder(node, level):
    global point
    if node.left != -1:
        inOrder(tree[node.left], level+1)
        
    nodes[level].append(point)
    point+=1
    
    if node.right != -1:
        inOrder(tree[node.right], level+1)

root = 0
for i in range(1, N+1):
    if parents[i] == 0:
        root = i

inOrder(tree[root], 1)

answer = 0
answerLevel = 0

keys = sorted(list(nodes.keys()))
for key in keys:
    width = nodes[key][-1] - nodes[key][0] + 1
    if width > answer:
        answer = width
        answerLevel = key
        
sys.stdout.write(str(answerLevel)+' '+str(answer))