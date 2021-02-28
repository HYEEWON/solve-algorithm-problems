from collections import defaultdict

def solution(participant, completion):
    answer = ''
    ret = defaultdict(int)
    for p in participant:
        ret[p] += 1
    for c in completion:
        ret[c] -= 1
    
    for key in ret.keys():
        if ret[key] > 0:
            answer = key
            break
    return answer