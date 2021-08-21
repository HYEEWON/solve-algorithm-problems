from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    finish = 0
    ing = deque()
    for i in range(bridge_length):
        ing.append(0)

    idx = 0
    total = 0
    while True:
        answer += 1
        tmp = ing.popleft()
        total -= tmp
        if tmp > 0:
            finish += 1
        if finish == len(truck_weights):
            break
        if idx < len(truck_weights) and total+truck_weights[idx] <= weight:
            ing.append(truck_weights[idx])
            total += truck_weights[idx]
            idx += 1
        else:
            ing.append(0)
        
    return answer

bridge_length = 2 
weight = 10
truck_weights = [7, 4, 5, 6]
print(solution(bridge_length, weight, truck_weights))