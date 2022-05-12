# 완전탐색, BFS/DFS 모두 가능
# n이 작기 떄문에 완전탐색도 가능함


from collections import deque
from copy import deepcopy

answer = []

def bfs(n, info):
    q = deque()
    # (인덱스, 점수) # 10점부터 맞춤
    q.append((0, [0 for i in range(11)]))
    max_gap = 0

    while q:
        focus, arrow = q.popleft()

        if sum(arrow) > n:
            continue
        elif sum(arrow) == n:  # 화살을 다 쏨
            apeach, lion = 0, 0
            # 점수 계산
            for i in range(11):
                if info[i] == 0 and arrow[i] == 0:
                    continue
                if info[i] > arrow[i]:
                    apeach += (10 - i)
                else:
                    lion += (10 - i)
            if lion > apeach:
                gap = lion - apeach
                if max_gap > gap:
                    continue
                if max_gap < gap:
                    max_gap = gap
                    answer.clear()
                answer.append(arrow)

        elif focus == 10: # 화살을 덜 쏴서 남은 화살을 다쏨
            tmp = deepcopy(arrow)
            tmp[focus] = n - sum(tmp)
            q.append((-1, tmp)) # focus 값이 더이상 필요 없어서 -1 대입
        else:
            # 어피치보다 화살을 1개 더 쏴서 점수를 얻음
            tmp = deepcopy(arrow)
            tmp[focus] = info[focus] + 1
            q.append((focus + 1, tmp))

            # 화살을 쏘지 않고 점수도 얻지 않음
            tmp2 = deepcopy(arrow)
            tmp2[focus] = 0
            q.append((focus + 1, tmp2))


def solution(n, info):
    bfs(n, info)

    if not answer:
        return [-1]
    else:
        return answer[-1] # 가장 낮은 점수를 더 많이 맞춘 경우