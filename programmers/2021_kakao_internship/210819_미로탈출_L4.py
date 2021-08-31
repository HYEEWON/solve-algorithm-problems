import heapq

def solution(n, start, end, roads, traps):
    start -=1; end -=1;
    graph = [[] for _ in range(n)]
    trap_dict = {trap-1:idx for idx, trap in enumerate(traps)};
    nodes = [];
    isVisit = [[False]*n for _ in range(1<<len(traps))]

    for road in roads: # 정방향: 0, 역방향: 1
        start_i, end_i, cost = road
        graph[start_i-1].append([end_i-1,cost,0])
        graph[end_i-1].append([start_i-1,cost,1])
    
    heapq.heappush(nodes,(0,start,0)) # cost, node, 방향

    print(trap_dict, graph)

    while nodes:
        cur_time, cur_node, state = heapq.heappop(nodes)
        if cur_node == end: 
            return cur_time;      
        if isVisit[state][cur_node] == True: 
            continue
        else: 
            isVisit[state][cur_node] = True
            
        for next_node, next_cost, road_type in graph[cur_node]:
            next_state = state
            cur_isTrap = 1 if cur_node in trap_dict else 0;
            next_isTrap = 1 if next_node in trap_dict else 0;

            if cur_isTrap == 0 and next_isTrap == 0: # 일반 -> 일반
                if road_type == 1: # 역방향
                    continue
            elif (cur_isTrap + next_isTrap) == 1: # 일반 -> 함정, 함정 -> 일반
                node_i = cur_node if cur_isTrap == 1 else next_node # 함정인 노드
                isTrapOn = (state & (1<<trap_dict[node_i]))>>trap_dict[node_i]
                print(next_node, next_cost, road_type, node_i, isTrapOn, "##########")
                print(state, node_i, trap_dict[node_i])
                if isTrapOn != road_type: continue
            else:
                isTrapOn = (state & (1<<trap_dict[cur_node]))>>trap_dict[cur_node]
                n_isTrapOn = (state & (1<<trap_dict[next_node]))>>trap_dict[next_node]
                print(next_node, next_cost, road_type, node_i, isTrapOn, n_isTrapOn) 
                if (isTrapOn ^ n_isTrapOn) != road_type: continue
            
            if next_isTrap == 1:
                next_state = state ^ (1<<trap_dict[next_node])

            heapq.heappush(nodes,(cur_time+next_cost, next_node, next_state))

## 다익스트라 풀이
# 23.1 / 100.0

'''def solution(n, start, end, roads, traps):
    graph = [[] for i in range(n+1)]
    for r in roads: # 갈 수 있음: 1, 갈 수 없음: 0
        graph[r[0]].append([r[1], r[2], 1])
        graph[r[1]].append([r[0], r[2], 0])

    cost = {node: sys.maxsize for node in range(1, n+1)}
    cost[start] = 0

    q = []
    heapq.heappush(q, (cost[start], start, True))

    while q:
        cur_cost, node, direc = heapq.heappop(q)
        if node == end:
            break
        if direc == False:
            for n in range(1, len(graph)):
                if n != node:
                    for k in range(len(graph[n])):
                        if graph[n][k][0] == node:
                            graph[n][k][2] = (graph[n][k][2]+1) % 2
                else:
                    for k in range(len(graph[n])):
                        graph[n][k][2] = (graph[n][k][2]+1) % 2

        for i in graph[node]:
            if i[2] == False:
                continue
            dist = cur_cost + i[1]
            cost[i[0]] = dist
            if i[0] in traps:
                heapq.heappush(q, (dist, i[0], False))
            else:
                heapq.heappush(q, (dist, i[0], True))   
    return cost[end]'''

#print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))