from collections import defaultdict
import collections import Counter
from functools import reduce

def solution(clothes):
    answer = 1
    d = defaultdict(int)
    for i in range(len(clothes)):
        d[clothes[i][1]] += 1
    val = list(d.values())
    for i in range(len(val)):
        answer *= (val[i]+1)
    return answer-1

def solution2(clothes):
    return reduce(lambda x,y:x*y,[a+1 for a in Counter([x[1] for x in clothes]).values()])-1

clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
print(solution(clothes))