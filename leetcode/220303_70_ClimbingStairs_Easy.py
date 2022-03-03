# DP
# 계단을 1, 2칸씩 오를 수 있을 경우, 오르는 경우의 수
# [i - 2]에서 [i]로 2칸 이동, [i - 1]에서 [i]로 1칸 이동

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        dp = [0 for i in range(n + 1)]
        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
    