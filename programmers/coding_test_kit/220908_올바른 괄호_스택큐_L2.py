# 스택과 큐를 사용하지 않고 숫자 더하기로 구현

def solution(s):
    v = 0
    for ss in s:
        v = v+1 if ss == '(' else v-1
        if v < 0:
            return False
    return True if v == 0 else False
