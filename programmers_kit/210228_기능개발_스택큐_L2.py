import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    days = deque()
    for i in range(len(progresses)):
        days.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    cnt, st = 0, 0
    while days:
        if cnt == 0:
            st = days.popleft()
            cnt += 1
        else:
            if days[0] <= st:
                days.popleft()
                cnt += 1
            else:
                answer.append(cnt)
                cnt = 0
    if cnt > 0:
        answer.append(cnt)

    return answer

print(solution([93, 30, 55], [1, 30, 5]))