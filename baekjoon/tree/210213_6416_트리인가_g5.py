import sys
from collections import defaultdict

def isTree():
    rootCnt = 0
    for key in outDegree:
        if key not in inDegree:
            rootCnt += 1
    if rootCnt > 1 or rootCnt == 0:
        return False

    for value in inCnt.values():
        if value > 1:
            return False
    
    # 트리: edge 수 + 1 == 노드 수
    if edgeCnt + 1 != len(outDegree | inDegree):
        return False
    return True

k = 1
while True:
    outDegree = set()
    inDegree = set()
    inCnt = defaultdict(int)
    edgeCnt = 0

    while True:
        flag = 1
        ins = list(sys.stdin.readline().strip().split("  "))
        if ins == ["-1 -1"]:
            flag = 2
            break
        for i in ins:
            i = i.split()
            if i[0] == i[1] == '0':
                flag = 0
                break
            outDegree.add(i[0])
            inDegree.add(i[1])
            inCnt[i[1]] += 1
            edgeCnt += 1
        if flag == 0:
            break
    if flag == 2:
            break

    if len(outDegree) == 0:
        sys.stdout.write("Case "+ str(k) + " is a tree.\n")
    elif isTree():
        sys.stdout.write("Case "+ str(k) + " is a tree.\n")
    else:
        sys.stdout.write("Case "+ str(k) + " is not a tree.\n")
    k+=1
    if sys.stdin.readline().strip() == "-1 -1":
        break