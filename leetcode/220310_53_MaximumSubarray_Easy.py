# Array, Dynamic Programming, Divide and Conquer

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[i] for i in range(len(nums))]
        answer = dp[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i], dp[i - 1] + nums[i])
            answer = max(answer, dp[i])

        return answer