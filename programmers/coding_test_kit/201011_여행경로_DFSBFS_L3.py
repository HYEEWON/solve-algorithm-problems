from collections import deque, defaultdict
import copy

ans = []
def dfs(node, road, N):
    global ans
    if len(ans) == N+1:
        return ans
    
    for idx, city in enumerate(road[node]):    
        ans.append(city)
        road[node].pop(idx)
        ret = dfs(city, road, N)           
        road[node].insert(idx, city)
        if ret:
            return ret
        ans.pop()

def solution(tickets):
    global ans
    road = defaultdict(list)
    for i in range(len(tickets)):
        road[tickets[i][0]].append(tickets[i][1])
        road[tickets[i][0]].sort() # 알파벳이 작은 것 부터
        
    ans.append('ICN')
    dfs('ICN', road, len(tickets))
    return ans