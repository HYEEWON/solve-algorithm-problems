# Array, Binary Search, DP, Greedy

# 참고 풀이
# https://leetcode.com/problems/split-array-largest-sum/discuss/89817/Clear-Explanation%3A-8ms-Binary-Search-Java
# https://leetcode.com/problems/split-array-largest-sum/discuss/1899144/Python-Clean-Code-oror-Parametric-Search

'''
1) m개 초과로 나눌 수 있음
  mid가 너무 작음 -> mid가 최대가 되기 위해서는 m보다 큰 숫자로 나눠야 함
  -> valid = False / low = mid + 1
2) m개 초과로 나눌 수 없음 (m개 이하로 나눌 수 있음)
  mid가 너무 큼 -> m개로 나누었을 때, 최대 값이 mid보다 작음 / m개 미만으로 나누어 최대 값이 mid 도달 가능
  -> valid = True / high = mid - 1
'''

import sys

class Solution:
    def splitArray(self, nums, m):
        low, high = max(nums), sum(nums)
        answer = sys.maxsize

        while low <= high:
            mid = (low + high) // 2
            if self.isValid(nums, m, mid):
                high = mid - 1
                answer = min(mid, answer)
            else:
                low = mid + 1

        return answer # 또는 low도 가능

    def isValid(self, nums, m, target):
        tot, cnt = 0, 1
        for n in nums:
            tot += n
            if tot > target:
                tot = n
                cnt += 1
                if cnt > m:
                    return False
        return True
