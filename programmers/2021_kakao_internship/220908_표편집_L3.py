# 연결 리스트
# 삽입/삭제 시간 복잡도: O(1)
# 딕셔너리에 [이전 값, 이후 값]을 저장해 연결 리스트처럼 사사용

# 스택
# 복원은 최근에 삭제한 것부터 복원하기 때문에 스택 사용

def solution(n, k, cmd):
    answer = ['O' for i in range(n)]
    stack = [] # 스택 # 복원에 사용
    linked_list = {} # 연결 리스트
    for i in range(1, n-1):
        linked_list[i] = [i-1, i+1]
    linked_list[0], linked_list[n-1] = [-1, 1], [n-2, -1]
    
    for c in cmd:
        if c == 'C':
            answer[k] = 'X'
            prev, next = linked_list[k]
            stack.append([k, prev, next])
            if next == -1:
                k = linked_list[k][0]
                linked_list[prev][1] = -1
            elif prev == -1:
                k = linked_list[k][1]
                linked_list[next][0] = -1
            else:
                k = linked_list[k][1]
                linked_list[prev][1] = next
                linked_list[next][0] = prev
        elif c == 'Z':
            num, prev, next = stack.pop()
            answer[num] = 'O'
            if prev == -1: # num == 0 으로 하면 안됨 # 1개만 삭제하는 것이 아님
                linked_list[next][0] = num
            elif next == -1: # num == n-1 으로 하면 안됨 # 1개만 삭제하는 것이 아님
                linked_list[prev][1] = num
            else:
                linked_list[prev][1] = num
                linked_list[next][0] = num
        else:
            op, num = c.split()
            if op == 'D':
                for i in range(int(num)):
                    k = linked_list[k][1]
            else:
                for i in range(int(num)):
                    k = linked_list[k][0]
    return ''.join(answer)
