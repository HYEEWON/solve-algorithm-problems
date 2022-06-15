# DFS, 구현
# DFS를 사용하지 않고, 반복문으로 해도 가능

from collections import defaultdict
import sys

sys.setrecursionlimit(100000)
index = defaultdict(int)

def dfs(i, person, enroll, referral, profit):
    global index

    tmp = int(profit[person][-1] * 0.1)
    profit[person][-1] = profit[person][-1] - tmp

    if tmp > 0 and referral[i] != '-':
        profit[referral[i]].append(tmp)
        dfs(index[referral[i]], referral[i], enroll, referral, profit)

def solution(enroll, referral, seller, amount):
    global index

    answer = []
    profit = defaultdict(list)

    for i, e in enumerate(enroll):
        index[e] = i
        profit[e] = []

    for i, e in enumerate(seller):
        profit[e].append(amount[i] * 100)
        dfs(index[e], e, enroll, referral, profit)

    for e in enroll:
        answer.append(sum(profit[e]))
    return answer