# 완전탐색, BFS/DFS 모두 가능
# n이 작기 떄문에 완전탐색도 가능함함

from collections import deque
from copy import deepcopy

def bfs(n, info):
    answer = []
    q = deque()
    q.append((0, [0 for i in range(11)]))
    max_gap = 0

    while q:
        focus, arrow = q.popleft()

        if sum(arrow) > n:
            continue
        elif sum(arrow) == n: # 화살을 다 쏨
            apeach, lion = 0, 0

            for i in range(11):
                if info[i] == 0 and arrow[i] == 0:
                    continue
                if info[i] > arrow[i]:
                    apeach += (10 - i)
                else:
                    lion += (10 - i)
            if lion > apeach:
                gap = lion - apeach
                if max_gap < gap:
                    max_gap = gap
                    answer.clear()

                answer.append(arrow)

        elif focus == 10:
            tmp = deepcopy(arrow)
            tmp[focus] = n - sum(tmp)
            q.append((-1, tmp))
        else:
            tmp = deepcopy(arrow)
            tmp[focus] = info[focus]+1
            q.append((focus+1, tmp))

            tmp2 = deepcopy(arrow)
            tmp2[focus] = 0
            q.append((focus+1, tmp2))

    return answer

def solution(n, info):
    bfs(n, info)
    print(answer)
    if not answer:
        return [-1]
    else:
        return answer[-1]

print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))