#(*) 참고한 풀이
# 무거운 사람부터 보트를 태워, 보트 사용을 최소화
from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    q = deque(people)

    while q:
        if len(q) >= 2:
            if q[0] + q[-1] <= limit:
                q.pop()
                q.popleft()
                answer += 1
            else:
                q.pop()
                answer += 1
        else:
            if q[0] <= limit:
                q.pop()
                answer += 1
    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))

# 20/100
'''
def solution(people, limit):
    answer = 0
    visit = [0] * len(people)
    while 0 in visit:
        weight = 0
        i = -1
        while i < len(people)-1:  
            i += 1
            if weight + people[i] <= limit:        
                if visit[i] == 0:   
                    weight += people[i]
                    visit[i] = 1    
        answer += 1
    return answer
'''