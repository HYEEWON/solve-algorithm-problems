# Array, Binary Search
# Binary Search로 O(logN) 해결

# 파이썬의 bisect를 이용할 수도 있음
# https://leetcode.com/problems/insert-interval/discuss/1444764/Python-Binary-Search

class Solution:
    def binary_search(self, intervals, target, idx):
        start, end = 0, len(intervals) - 1

        while start <= end:
            mid = (start + end) // 2
            if intervals[mid][0] <= target <= intervals[mid][1]:
                answer = mid
                break
            elif intervals[mid][idx] < target:
                start = mid + 1
            else:
                end = mid - 1

        else:
            if idx == 1: # s 구하기
                answer = start
            else: # e 구하기
                answer = end
        return answer

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        # 합쳐져야 되는 첫번째, 마지막 인터벌
        s, e = self.binary_search(intervals, newInterval[0], 1), self.binary_search(intervals, newInterval[1], 0)

        if s > e: # 합치지 않는 경우
            return intervals[:s] + [newInterval] + intervals[e+1:]
        return intervals[:s] + [[min(newInterval[0], intervals[s][0]), max(newInterval[1], intervals[e][1])]] + intervals[e+1:]
