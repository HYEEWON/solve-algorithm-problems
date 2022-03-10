# Tree, DFS/BFS, Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q) -> bool:
        if (not p and q) or (p and not q):
            return False
        if p != None and q != None:
            if p.val != q.val:
                return False
            if not self.isSameTree(p.left, q.left) or not self.isSameTree(p.right, q.right):
                return False
        return True

    # 구조 개선
    # 참고) https://leetcode.com/problems/same-tree/discuss/32847/Python-solution
    def isSameTree2(self, p, q) -> bool:
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False

        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
