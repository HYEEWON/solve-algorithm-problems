dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = -1

def isIn(y, x):
    global N, M
    if 0<y<=N and 0<x<=M:
        return True
    return False

def move(pos, cnt, N, M):
    global answer
    global maps
    if cnt > 10:
        return -1
    p1 = isIn(pos[0][0], pos[0][1])
    p2 = isIn(pos[1][0], pos[1][1])
    if not p1 and not p2:
        return -1
    if not p1 or not p2:
        if answer == -1:
            answer = cnt
        else:
            answer = min(answer, cnt)
        return
    ans = -1
    for i in range(4):
        ny1 = pos[0][0] + dy[i]
        nx1 = pos[0][1] + dx[i] 
        ny2 = pos[1][0] + dy[i]
        nx2 = pos[1][1] + dx[i] 
        if isIn(ny1, nx1) and maps[ny1][nx1] == '#':
            ny1, nx1 = pos[0][0], pos[0][1]
        if isIn(ny2, nx2) and maps[ny2][nx2] == '#':
            ny2, nx2 = pos[1][0], pos[1][1]
        if visit[ny1][nx1][ny2][nx2] == 0:
            visit[ny1][nx1][ny2][nx2] = 1
            move([[ny1, nx1], [ny2, nx2]], cnt+1, N, M)
            visit[ny1][nx1][ny2][nx2] = 0
            
N, M = map(int, input().split())
maps = []
pos=[]

maps.append(['.' for m in range(M+2)])
for n in range(N):
    ins = list('.'+input()+'.')
    maps.append(ins)
    if 'o' in ins:
        for m in range(M):
            if 'o' == ins[m+1]:
                pos.append([n+1, m+1])
                maps[n+1][m+1] = '.'
maps.append(['.' for m in range(M+2)])

visit = [[[[0]*(M+2) for i in range(N+2)] for j in range(M+2)] for k in range(N+2)]
visit[pos[0][0]][pos[0][1]][pos[1][0]][pos[1][1]] = 1

move(pos, 0, N, M)
if answer > 10:
    answer = -1
print(answer)


#
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def isIn(y, x):
    global N, M
    if 0<y<=N and 0<x<=M:
        return True
    return False

def move(pos, cnt, N, M):
    global maps
    if cnt > 10:
        return -1
    p1 = isIn(pos[0][0], pos[0][1])
    p2 = isIn(pos[1][0], pos[1][1])
    if not p1 and not p2:
        return -1
    if not p1 or not p2:
        return cnt
    ans = -1
    for i in range(4):
        ny1 = pos[0][0] + dy[i]
        nx1 = pos[0][1] + dx[i] 
        ny2 = pos[1][0] + dy[i]
        nx2 = pos[1][1] + dx[i] 
        
        if isIn(ny1, nx1) and maps[ny1][nx1] == '#':
            ny1, nx1 = pos[0][0], pos[0][1]
        if isIn(ny2, nx2) and maps[ny2][nx2] == '#':
            ny2, nx2 = pos[1][0], pos[1][1]
        if visit[ny1][nx1][ny2][nx2] == 0:
            visit[ny1][nx1][ny2][nx2] = 1
            ret = move([[ny1, nx1], [ny2, nx2]], cnt+1, N, M)
            visit[ny1][nx1][ny2][nx2] = 0
            if ret == -1:
                continue
            if ans == -1 or ans>ret:
                ans = ret
    return ans

N, M = map(int, input().split())
maps = []
pos=[]

maps.append(['.' for m in range(M+2)])
for n in range(N):
    ins = list('.'+input()+'.')
    maps.append(ins)
    if 'o' in ins:
        for m in range(M):
            if 'o' == ins[m+1]:
                pos.append([n+1, m+1])
                maps[n+1][m+1] = '.'
maps.append(['.' for m in range(M+2)])


visit = [[[[0]*(M+2) for i in range(N+2)] for j in range(M+2)] for k in range(N+2)]
visit[pos[0][0]][pos[0][1]][pos[1][0]][pos[1][1]] = 1

print(move(pos, 0, N, M))