class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_cnt, cnt = 1, 1
        nums.sort()

        last = nums[0]
        for i in range(1, len(nums)):
            if last + 1 == nums[i]:
                cnt += 1
                last = nums[i]
            elif last != nums[i]:
                cnt, last = 1, nums[i]
            max_cnt = max(max_cnt, cnt)
        return max_cnt