from collections import deque

## 정답 풀이
# 링크드 리스트 사용
# 틀린 이유: 삭제, 추가 시에 앞/뒤 노드도 저장해야 함

def solution(n, k, cmd):
    answer = ['O'] * n
    table = {i: [i - 1, i + 1] for i in range(0, n)}
    del_row = deque()

    for c in cmd:
        if c[0] == 'D':
            for _ in range(int(c[2:])):
                k = table[k][1]
        elif c[0] == 'U':
            for _ in range(int(c[2:])):
                k = table[k][0]
        elif c[0] == 'C':
            prev, next = table[k]
            del_row.append([prev, next, k])
            answer[k] = "X"

            if next == n:
                k = table[k][0]
            else:
                k = table[k][1]

            if prev == -1:
                table[next][0] = prev
            elif next == n:
                table[prev][1] = next
            else:
                table[prev][1] = next
                table[next][0] = prev
        elif c[0] == 'Z':
            prev, next, now = del_row.pop()
            answer[now] = "O"

            if prev == -1:
                table[next][0] = now
            elif next == n:
                table[prev][1] = now
            else:
                table[prev][1] = now
                table[next][0] = now
    return ''.join(answer)

## 처음 풀이
# 효율성에서 통과 실패

def up(n, k, table):
    cnt = 0
    while cnt < n:
        k -= 1
        if table[k] == 'O':
            cnt += 1
    return k

def down(n, k, table):
    cnt = 0
    while cnt < n:
        k += 1
        if table[k] == 'O':
            cnt += 1
    return k

def solution(n, k, cmd):
    answer = ['O'] * n
    table = [[i-1, i+1] for i in range(0, n)]
    for i in range(n):
        table.append

    del_row = deque()

    for i in range(len(cmd)):
        cmd[i] = cmd[i].split()

        if len(cmd[i]) > 1:
            act, num = cmd[i][0], int(cmd[i][1])
        else:
            act = cmd[i][0]

        if act == "U":
            k = up(num, k, answer)
        elif act == "D":
            k = down(num, k, answer)
        elif act == "C":
            answer[k] = "X"
            del_row.append(k)
            if k == n-1:
                k = up(1, k, answer)
            else:
                k = down(1, k, answer)
        else: #Z
            new_row = del_row.pop()
            answer[new_row] = "O"
    return ''.join(answer)


print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))