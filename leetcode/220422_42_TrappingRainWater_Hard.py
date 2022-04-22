# Array, Two Pointers, Stack, DP

# 참고 링크
# https://leetcode.com/problems/trapping-rain-water/discuss/17357/Sharing-my-simple-c%2B%2B-code%3A-O(n)-time-O(1)-space
# https://leetcode.com/problems/trapping-rain-water/discuss/178028/Stack-with-Explanation-(Java-Python-Scala)

class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        max_left, max_right = 0, 0
        left, right = 0, len(height) - 1

        while left < right:
            # 두 높이 중 낮은 높이만큼 채울 수 있음
            if height[left] <= height[right]:
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    answer += (max_left - height[left])
                left += 1
            else:
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    answer += (max_right - height[right])
                right -= 1

        return answer

