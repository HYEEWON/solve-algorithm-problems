# Array, Hash Table, Sorting
# 풀이: 딕셔너리 사용, Set 사용

from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numbers = defaultdict(int)

        for n in nums:
            numbers[n] += 1
            if numbers[n] > 1:
                return True
        return False