# 재귀, Hash Table

# Hash Table
# 키: 방 번호, 값: 가장 가까운 빈 방

import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

def find(num, room_use, answer):
    if room_use[num] == 0:
        answer.append(num)
        room_use[num] = num + 1
        return num + 1

    room_use[num] = find(room_use[num], room_use, answer)
    return room_use[num]

def solution(k, room_number):
    answer = []
    room_use = defaultdict(int)

    for i, r in enumerate(room_number):
        find(r, room_use, answer)

    return answer