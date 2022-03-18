# Array, Sorting
# 참고 풀이
# https://leetcode.com/problems/merge-intervals/discuss/1067545/Python-beats-90

class Solution:
    def merge(self, intervals):
        if not intervals or len(intervals) == 1:
            return intervals

        intervals.sort()
        answer = []
        for interval in intervals:
            if not answer or interval[0] > answer[-1][1]:
                answer.append(interval)
            else:
                answer[-1][1] = max(answer[-1][1], interval[1])
        return answer
