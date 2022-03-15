# Array, Counting, Hash Table, Heap, Sorting

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums).most_common()
        answer = []
        for i in range(k):
            answer.append(d[i][0])

        return answer