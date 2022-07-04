# math, simulation

import re
from collections import Counter


def is_alpha(s):
    p = re.compile('[A-Z]{2}')
    return True if p.search(s) else False


def solution(str1, str2):
    str1, str2 = str1.upper(), str2.upper()
    list1, list2 = [], []

    for i in range(len(str1) - 1):
        if is_alpha(str1[i:i + 2]):
            list1.append(str1[i:i + 2])
    for i in range(len(str2) - 1):
        if is_alpha(str2[i:i + 2]):
            list2.append(str2[i:i + 2])

    inter, union = 0, 0
    c1, c2 = Counter(list1), Counter(list2)

    for k1 in c1.keys():
        if k1 in c2.keys():
            inter += min(c1[k1], c2[k1])
            union += max(c1[k1], c2[k1])
        else:
            union += c1[k1]
    for k2 in c2.keys():
        if k2 not in c1.keys():
            union += c2[k2]

    return int(inter / union * 65536) if union != 0 else 65536


## 참고 풀이
def solution(str1, str2):
    s1 = [str1[i:i+2].upper() for i in range(len(str1) - 1) if str1[i:i+2].isalpha()]
    s2 = [str2[i:i+2].upper() for i in range(len(str2) - 1) if str2[i:i+2].isalpha()]

    if not s1 and not s2:
        return 65536

    c1, c2 = Counter(s1), Counter(s2)
    answer = int(sum((c1 & c2).values()) / sum((c1 | c2).values()) * 65536)
    return answer
