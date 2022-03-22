# Tree, Binary Search Tree, DFS/BFS

# 이진 탐색 트리: 부모의 왼쪽은 부모보다 작고, 부모의 오른쪽은 부모보다 큼
# InOrder로 탐색하면 K번째 노드를 알 수 있음

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

answer = 0
cnt = 0 # K번째를 Count하는 변수

class Solution:
    def dfs(self, root, k):
        global cnt, answer
        if cnt >= k:
            return answer

        if root.left:
            self.dfs(root.left, k)
        cnt += 1
        if cnt == k: # K번째인 경우
            answer = root.val
            return answer
        if root.right:
            self.dfs(root.right, k)
        return answer

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        global cnt, answer
        cnt = 0
        self.dfs(root, k)
        return answer