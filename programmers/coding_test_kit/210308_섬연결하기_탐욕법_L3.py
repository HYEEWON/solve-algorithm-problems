def solution(n, costs):
    answer = 0
    visit = set()
    costs = sorted(costs, key=lambda x: x[2])
    visit.add(costs[0][0])

    while len(visit) != n:
        for cost in costs:
            if cost[0] in visit and cost[1] in visit:
                continue
            if cost[0] in visit or cost[1] in visit:
                visit.update([cost[0], cost[1]])
                answer += cost[2]
                break
    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))