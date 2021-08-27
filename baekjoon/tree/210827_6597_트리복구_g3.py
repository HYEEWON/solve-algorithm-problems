import sys

def postorder(root, start, end):

    for i in range(start, end, 1):
        if preorder[root] == inorder[i]:
            postorder(root+1, start, i);
            postorder(root+i+1-start, i+1, end);
            sys.stdout.write(str(preorder[root]));

while True:
    ins = sys.stdin.readline()
    if ins == '':
        break

    preorder, inorder = ins.strip().split()

    preorder = list(preorder)
    inorder = list(inorder)

    postorder(0, 0, len(preorder))
    sys.stdout.write('\n');