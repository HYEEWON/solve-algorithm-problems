def solution(routes):
    answer = 0
    routes = sorted(routes, key=lambda x: x[1])
    flag = [False] * len(routes)

    for i in range(len(routes)):
        if flag[i]:
            continue
        pos = routes[i][1]
        flag[i] = True
        answer += 1
        for j in range(i+1, len(routes)):
            if routes[j][0] <= pos <= routes[j][1]:
                flag[j] = True
    return answer

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))