# 큐

from collections import deque 

def solution(queue1, queue2):
    answer = 0
    q1, q2 = deque(queue1), deque(queue2)
    
    sum1, sum2 = sum(q1), sum(q2)
    total_sum = sum1 +sum2
    if total_sum % 2 != 0: # 전체 합이 홀수이면 두 큐의 합이 같아질 수 없음
        return -1
    
    # 반복 횟수는 큐 길이 * 3 # 예시: [1, 1, 1, 1, 1] [1, 1, 1, 9, 1] 총 12번 이동
    while answer <= len(queue1)*3:
        if sum1 > sum2:
            q2.append(q1.popleft())
            sum1 -= q2[-1]
            sum2 += q2[-1]
            answer += 1
        elif sum1 < sum2:
            q1.append(q2.popleft())
            sum1 += q1[-1]
            sum2 -= q1[-1]
            answer += 1
        else:
            return answer
    return -1
  
 
# 참고한 풀이
# https://school.programmers.co.kr/learn/courses/30/lessons/118667/solution_groups?language=python3

