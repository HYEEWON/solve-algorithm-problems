# Array, Binary Search
# O(logN) -> 이분 탐색

class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums)-1
        answer = 5001

        while start <= end:
            mid = (start+end) // 2

            if nums[mid] >= nums[0]:
                start = mid + 1
                answer = min(nums[0], answer)
            else: # nums[mid] < nums[0]:
                end = mid - 1
                answer = min(nums[mid], answer)

        return answer

    #(*) 풀이 참고
    # https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/643667/python-bin-search

    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        while nums[lo] > nums[hi]:
            mid = (lo + hi) // 2
            if nums[mid] < nums[hi]:
                hi = mid # -1 안함
            else:
                lo = mid + 1
        return nums[lo]