# Hash Table

from collections import defaultdict

def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]

    d = defaultdict(set)
    index = defaultdict(int)

    for i, ids in enumerate(id_list):
        index[ids] = i

    for r in set(report):
        r = r.split()
        d[r[1]].add(r[0])

    for key, value in zip(d.keys(), d.values()):
        if len(value) >= k:
            for name in d[key]:
                answer[index[name]] += 1

    return answer