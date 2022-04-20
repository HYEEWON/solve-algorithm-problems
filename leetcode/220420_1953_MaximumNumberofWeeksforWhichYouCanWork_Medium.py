# Array, Greedy

# 참고 링크
# https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/discuss/1375390/Python-Solution-with-detailed-explanation-and-proof-and-common-failure-analysis

import heapq

class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        sum_m, max_m = sum(milestones), max(milestones)

        if sum_m - max_m >= max_m:
            return sum_m
        return 2*(sum_m-max_m)+1

    # 기존 풀이 # 시간 초과
    def numberOfWeeks(self, milestones: List[int]) -> int:
        answer = 0
        h = []
        for m in milestones:
            heapq.heappush(h, -m)

        while True:
            c, tmp_pop = 0, []
            while c < 2 and h:
                tmp_pop.append(heapq.heappop(h) + 1)
                c += 1
                answer += 1

            if c < 2:
                break

            for e in tmp_pop:
                if e < 0:
                    heapq.heappush(h, e)

        return answer
