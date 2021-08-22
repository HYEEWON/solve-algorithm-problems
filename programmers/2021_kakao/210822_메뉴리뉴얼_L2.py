from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for c in course:
        tmp = []

        for order in orders:
            comb = combinations(sorted(order), c)
            tmp += comb
        cnt = Counter(tmp)

        if cnt:
            max_cnt = max(cnt.values())
            if max_cnt < 2:
                continue
            
            for key, value in cnt.items():
                if cnt[key] == max_cnt:
                    answer.append(''.join(key))
    answer.sort()
    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))

