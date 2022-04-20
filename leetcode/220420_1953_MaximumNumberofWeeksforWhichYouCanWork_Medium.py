# Array, Greedy

# 참고 링크
# https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/discuss/1375390/Python-Solution-with-detailed-explanation-and-proof-and-common-failure-analysis

class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        sum_m, max_m = sum(milestones), max(milestones)

        if sum_m - max_m >= max_m:
            return sum_m
        return 2*(sum_m-max_m)+1
