# Array, Binary Search, DP

class Solution:
    def lengthOfLIS(self, nums):
        answer = []
        answer.append(nums[0])

        for i in range(1, len(nums)):
            if nums[i] > answer[-1]:
                answer.append(nums[i])
            else:
                idx = self.lower_bound(nums[i], answer)
                answer[idx] = nums[i]
        return len(answer)

    def lower_bound(self, n, array):
        start, end = 0, len(array)-1

        while start < end:
            mid = (start+end) // 2
            if n > array[mid]:
                start = mid + 1
            else:
                end = mid
        return end


s = Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))