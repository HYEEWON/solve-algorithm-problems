# DP
# coins 동전으로 amount의 금액을 만드는데 필요한 최소 동전 수

import sys

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [sys.maxsize for i in range(amount+1)]
        dp[0] = 0

        for money in range(1, amount+1):
            for i in range(len(coins)):
                if money >= coins[i]:
                    dp[money] = min(dp[money], dp[money-coins[i]]+1)

        print(dp)
        if dp[amount] == sys.maxsize:
            return -1
        return dp[amount]
