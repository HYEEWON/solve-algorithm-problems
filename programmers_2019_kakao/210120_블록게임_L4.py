#(*) 다시 진행한 풀이
def canFill(board, y, x): # 0인 칸을 채울 수 있는지 확인
    for i in range(y):
        if board[i][x] > 0:
            return False
    return True

def test(board, y, x, h, w): #기준 y, x와 세로, 가로 길이
    emptyCount = 0
    lastValue = -1
    try:
        for i in range(h):
            for j in range(w):
                if board[y+i][x+j] == 0:
                    if canFill(board, y+i, x+j) == False: return False
                    emptyCount += 1
                    if emptyCount > 2: return False
                else:
                    if lastValue != -1 and lastValue != board[y+i][x+j]:
                        return False
                    lastValue = board[y+i][x+j]
        for i in range(y, y+h):
            for j in range(x, x+w):
                board[i][j] = 0
        return True
    except:
        return False
    
def solution(board):
    answer = 0
    while True:
        cnt = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if test(board, i, j, 3, 2) or test(board, i, j, 2, 3):
                    cnt+=1            
        if cnt == 0:
            break
        answer += cnt
    return answer


# 실패한 풀이 25.0/100
from collections import Counter
def test1(board, y, x):
    testBoard = []
    tmp = []
    try:
        for i in range(3): # 3*2
            for j in range(2):
                tmp.append(board[y+i][x+j])
                if board[y+i][x+j] == 0:
                    return False
                if board[y+i][x+j] == 201:
                    testBoard.append(0)
                else:
                    testBoard.append(1)
        if len(Counter(tmp).keys()) > 3:
            return False
        if testBoard == [0, 1, 0, 1, 1, 1]:
            for i in range(3): # 3*2
                for j in range(2):
                    board[y+i][x+j] = 0
            return True
        return False
    except:
        return False
    
def test2(board, y, x):
    testBoard = []
    tmp = []
    try:
        for i in range(2): # 2*3
            for j in range(-2, 1):
                tmp.append(board[y+i][x+j])
                if board[y+i][x+j] == 0:
                    return False
                if board[y+i][x+j] == 201:
                    testBoard.append(0)
                else:
                    testBoard.append(1)
        if len(Counter(tmp).keys()) > 2:
            return False
        if testBoard in [[1, 0, 0, 1, 1, 1], [0, 1, 0, 1, 1, 1]]:
            for i in range(2):
                for j in range(-2, 1):
                    board[y+i][x+j] = 0
            return True
        return False
    except:
        return False
    
def test3(board, y, x):
    testBoard = []
    tmp = []
    try:
        for i in range(3): # 3*2
            for j in range(-1, 1):
                tmp.append(board[y+i][x+j])
                if board[y+i][x+j] == 0:
                    return False
                if board[y+i][x+j] == 201:
                    testBoard.append(0)
                else:
                    testBoard.append(1)
        if len(Counter(tmp).keys()) > 3:
            return False
        if testBoard == [1, 0, 1, 0, 1, 1]:
            for i in range(3):
                for j in range(-1, 1):
                    board[y+i][x+j] = 0
            return True
        return False
    except:
        return False

def test4(board, y, x):
    testBoard = []
    tmp = []
    try:
        for i in range(2): # 2*3
            for j in range(-1, 2):
                tmp.append(board[y+i][x+j])
                if board[y+i][x+j] == 0:
                    return False
                if board[y+i][x+j] == 201:
                    testBoard.append(0)
                else:
                    testBoard.append(1)
        if len(Counter(tmp).keys()) > 3:
            return False
        if testBoard == [0, 0, 1, 1, 1, 1]:
            for i in range(2): # 2*3
                for j in range(-1, 2):
                    board[y+i][x+j] = 0
            return True
        return False
    except:
        return False
    
def solution2(board):
    answer = 0
    col = [i for i in range(len(board[0]))]
    while True:
        if len(col) < 1:
            return answer
        for j in col[:]:  
            for i in range(len(board)-1):
                if board[i+1][j] <= 0 or board[i][j] > 0:
                    if i == len(board)-2:
                        if j in col:
                            col.remove(j)
                    continue
                else:
                    board[i][j] = 201 # 검은 블럭
                    if test1(board, i, j) or test2(board, i, j) or test3(board, i, j) or test4(board, i, j):
                        answer += 1
                        break
                    if board[i][j] == board[i+1][j] == 201 and j in col:
                        col.remove(j)
                    break
    return answer

board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]
print(solution([[2,2,0,0], [1,2,0,4], [1,2,0,4], [1,1,4,4] ])) #1
print(solution([[0, 0, 0, 0, 0], [1, 0, 0, 2, 0], [1, 2, 2, 2, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]])) #2
#print(solution(board))
#print(solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]
#,[0,0,0,2,2,0,0,0,0,0],[0,0,0,2,1,0,0,0,0,0],[0,0,0,2,1,0,0,0,0,0],[0,0,0,0,1,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]])) #1