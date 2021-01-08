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
    print(levels)
    order(nodes, levels, 0)
    return [preorder, postorder]

#(*)


nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(nodeinfo))