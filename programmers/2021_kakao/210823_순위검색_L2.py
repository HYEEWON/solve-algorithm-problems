from collections import defaultdict
from itertools import combinations
import bisect

def solution(info, query):
    info_dict = defaultdict(list)
    answer = []

    for i in range(len(info)):
        info[i] = info[i].split()

    for x in info:
        for i in range(5):
            for c in combinations(range(4), i):
                x_tmp = x[:-1].copy()
                for idx in c:
                    x_tmp[idx] = '-'
                key = ''.join(x_tmp)
                info_dict[key].append(int(x[-1]))
    
    for value in info_dict.values():
        value.sort()

    for i in range(len(query)):
        query[i] = query[i].replace(" and ", '')
        query[i] = query[i].split()

    for q in query:
        condition, n = q[0], q[1]
        if condition in info_dict.keys():
            numbers = info_dict[condition]
            answer.append(len(numbers) - bisect.bisect_left(numbers, int(n)))
        else:
            answer.append(0)
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))