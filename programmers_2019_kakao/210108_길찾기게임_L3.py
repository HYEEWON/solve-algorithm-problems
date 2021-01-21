import sys
sys.setrecursionlimit(10**6)

#(*)

preorder = list()
postorder = list()

def order(nodeList, levels, curLevel):
    n = nodeList[:]
    print(n)
    cur = n.pop(0)
    preorder.append(cur[0])
    if n:
        for i in range(len(n)):
            if n[i][1][1] == levels[curLevel+1]:
                print('## ', n, '##', cur)
                if n[i][1][0] < cur[1][0]:
                    order([x for x in nodeList if x[1][0]< cur[1][0]], levels, curLevel+1)
                else:
                    order([x for x in nodeList if x[1][0]> cur[1][0]], levels, curLevel+1)
    postorder.append(cur[0])

def solution(nodeinfo):
    levels = sorted(list({x[1] for x in nodeinfo}), reverse=True)
    nodes = sorted(list(zip(range(1, len(nodeinfo)+1),nodeinfo) ), key= lambda x: (-x[1][1], x[1][0]))    
    print(nodes)
    order(nodes, levels, 0)
    return [preorder, postorder]

#(*) 이진 트리 구현
import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        self.x = data[0][0]
        self.y = data[0][1]
        self.id = data[2]

def addNode(parent, child):
    if child.x < parent.x:
        if parent.left == None:
            parent.left = child
        else:
            addNode(parent.left, child)
    else: # child.x > parent.x
        if parent.right == None:
            parent.right = child
        else:
            addNode(parent.right, child)

answer = [[], []]
def pre_order(node):
    global answer
    if node == None: return;
    answer[0].append(node.id)
    pre_order(node.left)
    pre_order(node.right)

def post_order(node):
    global answer
    if node == None: return;
    post_order(node.left)
    post_order(node.right)
    answer[1].append(node.id)

def solution2(nodeinfo):
    nodes = [[node, node[1], nodeinfo.index(node)+1] for node in nodeinfo]
    nodes = sorted(nodes, key = lambda x: -x[1])

    root = Node(nodes[0])
    for i in range(1, len(nodes)):
        a = Node(nodes[i])
        
        addNode(root, Node(nodes[i]))
    
    pre_order(root)
    post_order(root)
    return answer

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(nodeinfo))