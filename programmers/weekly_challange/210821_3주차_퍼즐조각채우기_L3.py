from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

board_block = []
table_block = []

def find_block(board, flag, y, x, visit, min_y, min_x, max_y, max_x, cnt):
    q = deque()
    q.append([y, x])
    
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if not 0<=nx<len(board) or not 0<=ny<len(board):
                continue
            if visit[ny][nx] == 1:
                continue

            if board[ny][nx] == flag:
                visit[ny][nx] = 1
                q.append([ny, nx])
                min_y, min_x, max_y, max_x = min(min_y, ny), min(min_x, nx), max(max_y, ny), max(max_x, nx)
                cnt += 1
    return min_y, min_x, max_y, max_x, cnt        

def rotate_90(block):
    rot = []
    for i in range(len(block[0])):
        tmp = []
        for j in range(len(block)-1, -1, -1):
            tmp.append(block[j][i])
        rot.append(tmp)
    return rot

def solution(game_board, table):
    answer = 0
    visit = [[0 for i in range(len(game_board))] for j in range(len(game_board))]
    visit2 = [[0 for i in range(len(table))] for j in range(len(table))]

    for i in range(len(game_board)):
        for j in range(len(game_board)):
            if game_board[i][j] == 0 and visit[i][j] == 0:
                visit[i][j] = 1
                min_y, min_x, max_y, max_x, cnt = i, j, i, j, 1
                min_y, min_x, max_y, max_x, cnt = find_block(game_board, 0, i, j, visit, min_y, min_x, max_y, max_x, cnt)
                board_block.append([min_y, min_x, max_y, max_x, cnt])
            if table[i][j] == 1 and visit2[i][j] == 0:
                visit2[i][j] = 1
                min_y2, min_x2, max_y2, max_x2, cnt2 = i, j, i, j, 1
                min_y2, min_x2, max_y2, max_x2, cnt2 = find_block(table, 1, i, j, visit2, min_y2, min_x2, max_y2, max_x2, cnt2)
                table_block.append([min_y2, min_x2, max_y2, max_x2, cnt2])

    for block in board_block:
        min_y, min_x, max_y, max_x, cnt = block
        board_blk = [row[min_x:max_x+1] for row in game_board[min_y:max_y+1]]
        for block2 in table_block[:]:
            min_y2, min_x2, max_y2, max_x2, cnt2 = block2
            table_blk = [row[min_x2:max_x2+1] for row in table[min_y2:max_y2+1]]

            comp_flag = False
            for i in range(4):
                same_flag = True
                
                if len(board_blk) == len(table_blk) and len(board_blk[0]) == len(table_blk[0]) and cnt == cnt2:
                    for y in range(len(board_blk)):
                        sum_tmp = -1
                        for x in range(len(board_blk[0])):
                            sum_tmp = board_blk[y][x] + table_blk[y][x] 
                            if sum_tmp != 1:
                                same_flag = False
                                break
                        if sum_tmp != 1:
                            same_flag = False
                            break
                    if same_flag:
                        answer += cnt
                        table_block.remove(block2)
                        comp_flag = True
                        break
                table_blk = rotate_90(table_blk)
            if comp_flag:
                break
    return answer


print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]))
print(solution([[0,0,0],[1,1,0],[1,1,1]], [[1,1,1],[1,0,0],[0,0,0]]))

