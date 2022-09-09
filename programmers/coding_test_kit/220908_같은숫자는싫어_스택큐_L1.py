# 스택
# 스택의 마지막 원소가 현재 원소와 다르다면 스택에 추가

def solution(arr):
    answer = []
    answer.append(arr[0])
    for a in arr[1:]:
        if answer and answer[-1] != a:
            answer.append(a)
    return answer
