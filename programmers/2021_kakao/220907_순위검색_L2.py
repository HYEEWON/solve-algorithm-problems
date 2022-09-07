# 정확성과 효율성이 모두 있는 문제

# 가능한 경우의 수를 모두 검색
# 해시 맵 사용
# 점수는 Lower Bound로 계산

from collections import defaultdict
from itertools import combinations
import bisect # Lower Bound

def solution(info, query):
    answer, total_dict = [], defaultdict(list)
    combi = []
    for i in range(5):
        combi += list(combinations(range(4), i))
    
    for i, val in enumerate(info):
        info[i] = val.split()
        info[i][-1] = int(info[i][-1])
        
        for c in combi:
            tmp_key = ''
            for idx in range(4):
                if idx not in c:
                    tmp_key += info[i][idx]
                else:
                    tmp_key += '-'
            total_dict[tmp_key].append(info[i][-1])
    
    for key in total_dict.keys():
        total_dict[key].sort()
        
    for i, val in enumerate(query):
        query[i] = val.replace('and', '').split()  
        key = ''.join(query[i][:4])
        answer.append(len(total_dict[key]) - bisect.bisect_left(total_dict[key], int(query[i][4])))
    return answer