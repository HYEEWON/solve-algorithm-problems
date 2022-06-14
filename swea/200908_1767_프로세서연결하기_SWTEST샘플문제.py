from collections import deque

# 큐를 사용했으나 dfs 특성상 pop을 하지 못해 배열과 같은 효과 발생..
T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(core_idx, line_len, core_num):
    global min_line, max_core
    if core_idx == len(core):  # 모든 코어 연결 성공
        if core_num > max_core:
            max_core = core_num
            min_line = line_len
        elif core_num == max_core:
            if min_line > line_len:
                min_line = line_len
        return

    y, x = core[core_idx]
    mem_visit = [[0 for i in range(N)] for j in range(N)]
    for n in range(N):
        for m in range(N):
            mem_visit[n][m] = visit[n][m]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        tmp_len = 0
        line_success = True
        while True:
            if ny < 0 or nx < 0 or ny > N - 1 or nx > N - 1:  # 벽까지 연결
                break
            if visit[ny][nx] == 1 or visit[ny][nx] == 2:  # core 이거나 전선 #더이상 연결 불가
                line_success = False
                break
            # 벽까지 연결될 수 있는지 검사 #i가 변하지 않으므로 한방향으로 증가
            visit[ny][nx] = 2
            nx += dx[i]
            ny += dy[i]
            tmp_len += 1
        if line_success:
            dfs(core_idx + 1, line_len + tmp_len, core_num + 1)
        for n in range(N):
            for m in range(N):
                visit[n][m] = mem_visit[n][m]
    # core에서 연결 불가
    dfs(core_idx + 1, line_len, core_num)


for test_case in range(1, T + 1):
    N = int(input())
    board = []
    visit = [[0 for i in range(N)] for j in range(N)]

    for n in range(N):
        # line = list(map(int, f.readline().split()))
        line = list(map(int, input().split()))
        board.append(line)

    core = deque([])
    core_idx = 0  # core 인덱스
    line_len = 0  # 전선 수
    core_num = 0  # 사용 core 수
    for y in range(N):
        for x in range(N):
            if board[y][x] == 1:
                visit[y][x] = 1
                if 1 <= y < N - 1 and 1 <= x < N - 1:
                    core.append([y, x])  # y: 세로, x: 가로
                else:
                    core_num += 1

    min_line = 150
    max_core = 0
    dfs(core_idx, line_len, core_num)
    print('#' + str(test_case) + ' ' + str(min_line))