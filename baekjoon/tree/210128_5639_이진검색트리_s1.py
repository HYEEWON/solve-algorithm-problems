import sys
sys.setrecursionlimit(20_000)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def addNode(parent, child):
    if child.data < parent.data:
        if parent.left == None:
            parent.left = child
        else:
            addNode(parent.left, child)
    else:
        if parent.right == None:
            parent.right = child
        else:
            addNode(parent.right, child)

def postOrder(node):
    if node.left != None:
        postOrder(node.left)
    if node.right != None:
        postOrder(node.right)
    sys.stdout.write(str(node.data)+'\n')


cnt = 0
while cnt <= 10000:
    try:
        n = int(sys.stdin.readline().strip())
        if cnt == 0:
            root = Node(n)
        else:
            addNode(root, Node(n))
        cnt += 1
    except:
        break

postOrder(root)