# Array, Two Pointers, String

import sys


class Solution:
    def threeSumClosest(self, nums, target):
        answer = 0
        diff = sys.maxsize
        nums.sort()
        for i in range(len(nums)):
            p1, p2 = i+1, len(nums)-1

            while 0 <= p1 < p2 < len(nums):
                three_sum = nums[i] + nums[p1] + nums[p2]

                if three_sum == target:
                    return target

                if diff > abs(three_sum - target):
                    diff = abs(three_sum - target)
                    answer = three_sum

                if three_sum > target:
                    p2 -= 1
                elif three_sum < target:
                    p1 += 1
        return answer
