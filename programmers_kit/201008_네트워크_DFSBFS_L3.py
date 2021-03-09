answer = 0
def dfs(cnt, start, n, computers, visit):
    global answer
    if cnt == n:
        return
    
    for i in range(n):
        if visit[i] == 0 and start != i and computers[start][i] == 1:
            visit[i] = 1
            dfs(cnt+1, i, n, computers, visit)
    
def solution(n, computers):
    global answer
    visit = [0 for i in range(n)]
    for i in range(n):
        if visit[i] == 0:
            answer += 1
            dfs(0, i, n, computers, visit)
    return answer