# Array, DP, Greedy

class Solution:
    # 참고 자료
    # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/discuss/208241/Explanation-for-the-dummy-like-me.
    def maxProfit(self, prices):
        answer = 0
        i, buy, sell = 0, 0, 0
        while i < len(prices)-1:
            # 감소할 때의 최소 값으로 구매
            while i<len(prices)-1 and prices[i+1]<=prices[i]:
                i += 1
            buy = prices[i]

            # 증가할 때의 최대 값으로 구매
            while i<len(prices)-1 and prices[i+1]>prices[i]:
                i += 1
            sell = prices[i]

            answer += (sell - buy)
        return answer

    # 참고 자료
    # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/discuss/306427/Different-Python-solutions-with-thinking-process
    def maxProfit2(self, prices):
        answer = 0
        for i in range(1, len(prices)):
            answer += max(prices[i+1]-prices[i], 0)
        return answer
