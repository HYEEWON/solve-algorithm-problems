# Tree, BFS/DFS, Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, root, cnt):
        if not root:
            return cnt
        return max(self.dfs(root.left, cnt + 1), self.dfs(root.right, cnt + 1))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)


    # 다른 풀이
    # https://leetcode.com/problems/maximum-depth-of-binary-tree/discuss/139585/Explanations-in-Python
    def maxDepth2(self, root):
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1