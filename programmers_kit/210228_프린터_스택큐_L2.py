from collections import deque

def solution(priorities, location):
    answer = 0
    for i in range(len(priorities)):
        priorities[i] = [priorities[i], i]
    priorities = deque(priorities)

    while priorities:
        p = priorities.popleft()
        flag = True
        for ps in priorities:
            if p[0] < ps[0]:
                flag = False
                priorities.append(p)
                break
        if flag == True:
            answer += 1
            if p[1] == location:
                break
    return answer

#(#) any를 사용한 풀이
def solution2(priorities, location):
    answer = 0
    priorities = [(v, i) for i, v in enumerate(priorities)]
    priorities = deque(priorities)

    while priorities:
        p = priorities.popleft()
        
        if any(p[0] < ps[0] for ps in priorities):
            priorities.append(p)
        else:
            answer += 1
            if p[1] == location:
                break
    return answer

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))