# Greedy, DP

# 틀린 이유
# max로만 이동할 수 있도록 코딩

class Solution:

    # 참고
    # https://leetcode.com/problems/jump-game/discuss/271858/Python-Greedy
    def canJump(self, nums: List[int]) -> bool:
        max_idx = 0

        for i in range(len(nums)):
            if max_idx < i:
                return False
            max_idx = max(max_idx, i + nums[i])

        return True
