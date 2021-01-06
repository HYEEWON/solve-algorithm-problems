import heapq
def solution(jobs):
    answer = 0
    start = -1 # 특정 작업의 시작 시간
    time = 0 # 전체 소요 시간
    heapq.heapify(jobs)
    heap = []
    cnt = 0
    while cnt<len(jobs):
        for job in jobs:
            if start < job[0] <= time:
                heapq.heappush(heap, (job[1], job[0])) # 소요시간 기준
        if len(heap):
            job = heapq.heappop(heap)
            answer += (time+job[0]-job[1])
            start = time
            time += job[0]
            cnt += 1
        else:
            time += 1
        
    return answer // len(jobs)

# 시간초과
from itertools import permutations
def solution2(jobs):
    per = permutations(jobs)
    answer = -1
    for p in per:
        ans = 0
        t = 0
        for job in p:
            if job[0] < t:
                ans += (t+job[1]-job[0])
                t += job[1]
            else:
                ans += (job[1])
                t = job[0]+job[1]
        if answer == -1:
            answer = ans
        else:
            answer = min(answer, ans)
    return answer//len(jobs)

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))