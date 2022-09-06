# 백트랙킹

N = int(input())
col = [0 for i in range(N)] # col[i]: i행에 있는 퀸의 열

def promising(n):
    for i in range(n):
        if (col[i] == col[n] or abs(col[i]-col[n]) == abs(i-n)):
            return False
    return True

def dfs(row, N): # 퀸을 놓는 행
    global answer
    if row == N:
        answer += 1
        return
    for i in range(N):
        col[row] = i
        if promising(row):
            dfs(row+1, N)

answer = 0
dfs(0, N) 
print(answer)