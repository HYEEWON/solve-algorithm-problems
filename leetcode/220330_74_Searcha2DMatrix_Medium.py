# Array, Binary Search, Matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        idx = self.binary_search1(matrix, target)
        if idx < 0:
            return False
        return self.binary_search2(matrix, idx, target)

    def binary_search1(self, matrix, target):
        start, end = 0, len(matrix)-1

        while start <= end:
            mid = (start+end)//2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return mid
            elif matrix[mid][0] > target:
                end = mid-1
            else:
                start = mid+1
        return -1

    def binary_search2(self, matrix, idx, target):
        start, end = 0, len(matrix[0]) - 1

        while start <= end:
            mid = (start + end) // 2
            if matrix[idx][mid] == target:
                return True
            elif matrix[idx][mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False