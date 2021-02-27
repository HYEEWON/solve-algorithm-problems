import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
# 앞 -> 루트 -> 뒤, 앞 -> 뒤 -> 루트 # 루트 -> 앞 -> 뒤
inorder, postorder = [0], [0]
inorder.extend(list(map(int, sys.stdin.readline().strip().split()))) 
postorder.extend(list(map(int, sys.stdin.readline().strip().split()))) 

idx = [0] * (n+1)
print(idx)
print(inorder)
print(postorder)
for i in range(n+1):
    #print(inorder[i], i)
    idx[inorder[i]] = i

def dfs(inStart, inEnd, postStart, postEnd):
    print(inStart, inEnd, postStart, postEnd)
    if inStart>inEnd or postStart>postEnd:
        return

    root = postorder[postEnd]
    #sys.stdout.write(str(root)+' ')
    print(root)

    dfs(inStart, idx[root]-1, postStart, postStart+(idx[root]-inStart)-1)
    dfs(idx[root]+1, inEnd, postStart+(idx[root]-inStart), postEnd-1)

dfs(1, n, 1, n)


'''import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
# 앞 -> 루트 -> 뒤, 앞 -> 뒤 -> 루트 # 루트 -> 앞 -> 뒤
inorder = list(map(int, sys.stdin.readline().strip().split())) 
postorder = list(map(int, sys.stdin.readline().strip().split())) 


def dfs(inStart, inEnd, postStart, postEnd):
    print(inStart, inEnd, postStart, postEnd)
    if inStart>inEnd or postStart>postEnd:
        return

    root = postorder[postEnd]
    #sys.stdout.write(str(root)+' ')
    print(root)
    index = inorder.index(root)-inStart

    dfs(inStart, inStart+index-1, postStart, postStart+index-1)
    dfs(inStart+index+1, inEnd, postStart+index, postEnd-1)


dfs(0, n-1, 0, n-1)'''