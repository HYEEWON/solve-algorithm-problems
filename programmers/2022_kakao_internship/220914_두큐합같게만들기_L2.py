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
  
 
# 참고 풀이
# https://school.programmers.co.kr/learn/courses/30/lessons/118667/solution_groups?language=python3

# 투 포인터
# 두개의 큐를 이용하는 것이 아니라 1개 큐로 계산
# 큐는 순서가 유지되기 때문에 가능
def solution(queue1, queue2):
    q = queue1 + queue2
    total_sum = sum(q)
    if total_sum % 2 != 0:
        return -1
        
    target_sum = total_sum // 2
    half_sum = sum(queue1)
    start, end, answer = 0, len(queue1)-1, 0
    
    while end < len(q):
        if half_sum > target_sum:
            half_sum -= q[start]
            start += 1
            answer += 1
        elif half_sum < target_sum:
            end += 1
            if end == len(q):
                return -1
            half_sum += q[end]
            answer += 1
        else:
            return answer
    return -1
