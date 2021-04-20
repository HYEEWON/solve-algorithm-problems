import sys
import copy
input = sys.stdin.readline

N = int(input())
board = []
for i in range(N):
    board.append(list(map(int, input().strip().split())))

answer = 0

def move(direction):
    global N
    change = [[0 for i in range(N)] for j in range(N)]

    if direction == 0: #위
        for i in range(1, N):
            for j in range(N):
                idx = i
                while board[idx-1][j] == 0 and idx>0:
                    idx -= 1
                if idx != i:
                    board[idx][j] = board[i][j]
                    board[i][j] = 0

                if idx > 0:
                    if board[idx][j] == board[idx-1][j] and change[idx-1][j] == 0:
                        change[idx-1][j] = 1
                        board[idx-1][j] = 2 * board[idx-1][j]
                        board[idx][j] = 0
    
    elif direction == 1: #왼
        for i in range(1, N):
            for j in range(N):
                idx = i
                while board[j][idx-1] == 0 and idx>0:
                    idx -= 1
                if idx != i:
                    board[j][idx] = board[j][i]
                    board[j][i] = 0
    
                if idx > 0:
                    if board[j][idx] == board[j][idx-1] and change[j][idx-1] == 0:
                        change[j][idx-1] = 1
                        board[j][idx-1] = 2 * board[j][idx-1]
                        board[j][idx] = 0 
                
    elif direction == 2: #아래
        for i in range(N-2, -1, -1):
            for j in range(N):
                idx = i
                while idx<N-1 and board[idx+1][j] == 0:
                    idx += 1
                if idx != i:
                    board[idx][j] = board[i][j]
                    board[i][j] = 0

                if idx < N-1:
                    if board[idx][j] == board[idx+1][j] and change[idx+1][j] == 0:
                        change[idx+1][j] = 1
                        board[idx+1][j] = 2 * board[idx+1][j]
                        board[idx][j] = 0 
                    
    elif direction == 3: #오른
        for i in range(N-2, -1, -1):
            for j in range(N):
                idx = i
                while idx<N-1 and board[j][idx+1] == 0:
                    idx += 1
                if idx != i:
                    board[j][idx] = board[j][i]
                    board[j][i] = 0

                if idx < N-1:
                    if board[j][idx] == board[j][idx+1] and change[j][idx+1] == 0:
                        change[j][idx+1] = 1
                        board[j][idx+1] = 2 * board[j][idx+1]
                        board[j][idx] = 0  

def dfs(cnt):
    global board, N, answer
    if cnt >= 5:
        for i in range(N):
            answer = max(answer, max(board[i]))
        return

    tmp_board = copy.deepcopy(board)
    for i in range(4):
        move(i)
        dfs(cnt+1)
        board = copy.deepcopy(tmp_board)

dfs(0)
sys.stdout.write(str(answer))