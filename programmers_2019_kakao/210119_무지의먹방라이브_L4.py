def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    if k<len(food_times):
        return k+1
    
    food = dict()
    for i in range(len(food_times)):
        food[i] = food_times[i]

    while True:
        #print(len(food.keys()))
        remain = k % len(food.keys())
        time = k // len(food.keys())
        print(remain, time, food, k)
        if time <= 0:
            cnt = 0
            for key in list(food.keys())[:]:
                if cnt == remain:
                    return key+1
                food[key] -=1
                cnt += 1
                
        #k -= len(food)*time
        for key in list(food.keys())[:]:
            food[key] -= time
            if food[key] <= 0:
                remain += abs(food[key])
                del food[key]
        k = remain
        print(remain, time, food, k, end='\n\n')
    return -1

print("s:", solution([4, 1, 1, 5], 4))
print(solution([4, 2, 3, 6, 7, 1, 5, 8],27))
print(solution([4, 2, 3, 6, 7, 1, 5, 8], 16))
print(solution([3, 1, 2], 5))