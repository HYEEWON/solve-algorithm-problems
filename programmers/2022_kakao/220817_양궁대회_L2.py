# backtracking, bfs, combination 모두 가능
# 모든 경우의 수를 다 해봐야 함

from copy import deepcopy

answer = [-1]
max_gap = 0

def back_tracking(n, info, arrow, idx):
    global answer, max_gap
    if sum(arrow) > n:
        return
    elif sum(arrow) == n:
        apeach, lion = 0, 0
        for i in range(11):
            if info[i] == 0 and arrow[i] == 0:
                continue
            if info[i] >= arrow[i]:
                apeach += (10-i)
            else:
                lion += (10-i)
        if lion > apeach and lion - apeach > max_gap:
            max_gap = lion - apeach
            answer = deepcopy(arrow)
        elif lion > apeach and lion - apeach == max_gap:
            flag = False
            for i in range(10, -1, -1):
                if arrow[i] > answer[i]:
                    flag = True
                    break
                if arrow[i] < answer[i]:
                    break
            if flag:
                max_gap = lion - apeach
                answer = deepcopy(arrow)
        return
    if idx > 10:
        return
    if idx == 10:
        arrow[idx] = n - sum(arrow)
    else:
        arrow[idx] = info[idx] + 1
    back_tracking(n, info, arrow, idx+1)
    arrow[idx] = 0
    back_tracking(n, info, arrow, idx+1)

def solution(n, info):
    global answer
    back_tracking(n, info, [0 for i in range(11)], 0)
    return answer