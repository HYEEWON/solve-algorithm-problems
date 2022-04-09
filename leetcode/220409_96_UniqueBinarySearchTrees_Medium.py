# Math, DP, Tree, Binary Search Tree

# 참고 링크
# https://leetcode.com/problems/unique-binary-search-trees/discuss/164915/Python-solution

'''
    루트: i
    왼쪽 서브 트리: 1 ~ i-1 (i-1), 오른쪽 서브 트리: i+1 ~ n (n-i)

    F(r, n): 루트가 r, 노드가 1~n인 BST의 개수
    G(n) = F(1, n) + F(2, n) + ... + F(n, n)
    G(0)=1, G(1)=1 // 트리가 비었거나 루트만 존재하는 경우

    F(i, n) = G(i-1) * G(n-i)	1 <= i <= n
    G(n) = G(0) * G(n-1) + G(1) * G(n-2) + … + G(n-1) * G(0)
'''

class Solution:

    def numTrees(self, n):
        dp = [0 for i in range(n+1)]
        dp[0] = dp[1] = 1

        for i in range(2, n+1): # 노드 수
            for root in range(1, i+1): # 루트
                dp[i] += dp[root-1] * dp[i-root]
        return dp[n]


    def numTrees_recursive(self, n: int) -> int:
        if n == 0:
            return 1

        answer = 0
        for i in range(1, n+1):
            answer += self.numTrees(i-1)*self.numTrees(n-i)
        return answer

s = Solution()
print(s.numTrees(5))