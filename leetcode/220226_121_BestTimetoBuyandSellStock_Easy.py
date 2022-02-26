# Array, DP

class Solution:
    def maxProfit(prices):
        answer = 0
        min_buy = prices[0]

        for i in range(1, len(prices)):
            min_buy = min(min_buy, prices[i])
            answer = max(answer, prices[i] - min_buy)

        return answer

        '''
        dp = [0 for i in range(len(prices))]
        min_buy = prices[0]

        for i in range(1, len(prices)):
            if prices[i] - min_buy > 0:
                dp[i] = max(dp[i - 1], prices[i] - min_buy)
            if min_buy > prices[i]:
                min_buy = prices[i]
                max_sell = 0
            dp[i] = max(dp[i - 1], dp[i])
        return dp[len(prices) - 1]
        '''
