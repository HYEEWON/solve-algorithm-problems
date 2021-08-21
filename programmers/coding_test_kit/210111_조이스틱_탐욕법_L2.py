# (*)
## 같은 것을 문자열로 구현하면 시간 초과
def solution(name):
    flag = [min(ord(name[i]) - ord('A'), 91 - ord(name[i])) for i in range(len(name))]

    answer, i = 0, 0
    while True:
        answer += flag[i]
        flag[i] = 0
        if flag.count(0) == len(name):
            return answer
        front, back = 1, 1
        while flag[i+back] == 0:
            back += 1
        while flag[i-front] == 0:
            front += 1
        answer += front if front < back else back
        i += -front if front < back else back       
    return answer

# 시간 초과
def solution2(name):
    answer = 0
    flag = [False for i in range(len(name))]
    for i in range(len(flag)):
        if name[i] == 'A':
            flag[i] = True
    i = 0
    while True:
        if name[i] != 'A':
            answer += min(ord(name[i]) - ord('A'), 91 - ord(name[i]))
            flag[i] = True

        if flag.count(True) == len(name):
            return answer
        cnt = 0
        while True:
            back = i + 1
            front = i - 1
            cnt += 1
            if back >= len(name):
                back -= len(name)
            if front < 0:
                front += len(name)
            if flag[back] != '1':
                i = back
                answer += cnt
                break
            elif flag[front] != '1':
                i = front
                answer += cnt
                break        
    return answer

name = 'JEROEN' # 9 + 4 + 9 + 12 + 4 + 13 #'JAZ'
print(solution(name))
