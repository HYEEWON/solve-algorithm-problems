import sys

answer = []

def postorder(root, start, end):
    for i in range(start, end):
        if preorder[root] == inorder[i]:
            postorder(root+1, start, i)
            postorder(root+i-start+1, i+1, end)
            answer.append(str(preorder[root]))
    
T = int(sys.stdin.readline())

for t in range(T):
    answer = []
    n = int(sys.stdin.readline())

    preorder = list(map(int, sys.stdin.readline().strip().split()))
    inorder = list(map(int, sys.stdin.readline().strip().split()))

    root = preorder[0]
    postorder(0, 0, n)
    sys.stdout.write(" ".join(answer) + "\n")