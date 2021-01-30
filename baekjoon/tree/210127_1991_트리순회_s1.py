import sys

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def preOrder(node):
    sys.stdout.write(str(node.data))
    if node.left != '.':
        preOrder(tree[node.left])
    if node.right != '.':
        preOrder(tree[node.right])

def inOrder(node):
    if node.left != '.':
        inOrder(tree[node.left])
    sys.stdout.write(str(node.data))
    if node.right != '.':
        inOrder(tree[node.right])

def postOrder(node):
    if node.left != '.':
        postOrder(tree[node.left])
    if node.right != '.':    
        postOrder(tree[node.right])
    sys.stdout.write(str(node.data))

N = int(input())
nodes = []
tree = {}
for i in range(N):
    node, left, right = input().split()
    tree[node] = Node(node, left, right)

preOrder(tree['A'])
print()
inOrder(tree['A'])
print()
postOrder(tree['A'])