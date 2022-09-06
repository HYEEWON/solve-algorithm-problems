import sys

R, C = map(int, sys.stdin.readline().strip().split())
board = []

for i in range(R):
    board.append(list(sys.stdin.readline().strip()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0
alpha = [0 for i in range(27)]

def dfs(y, x, cnt): # 세로, 가로
    flag = False
    global answer
    if cnt >= 26:
        answer = max(answer, cnt)
        return answer

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or ny<0 or nx>=C or ny>=R:
            continue
        
        ascii_ = ord(board[ny][nx])-65
        if alpha[ascii_] == 0:
            flag = True
            alpha[ascii_] = 1
            dfs(ny, nx, cnt+1)
            alpha[ascii_] = 0
        if answer >= 26:
            return answer
    if flag == False:        
        answer = max(answer, cnt)
    return answer

alpha[ord(board[0][0])-65] = 1
sys.stdout.write(str(dfs(0, 0, 1)))