# Array, Binary Search

# 못 푼 이유: 이분 탐색이라는 것은 알았으나 범위 변경에 실패

class Solution:
    def search(self, nums, target):
        return self.binary_search(nums, target)

    def binary_search(self, nums, target):
        start, end = 0, len(nums)-1

        while start <= end:
            mid = (start+end) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[end] and target < nums[start]:
                return -1
            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1

s = Solution()
print(s.search([5,1,3], 5))
#print(s.search([4,5,6,7,0,1,2], 2))