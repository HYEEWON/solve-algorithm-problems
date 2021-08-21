from collections import Counter

def solution(n, lost, reserve):
    student = [1 for i in range(n)]
    for l in lost:
        student[l-1] -= 1
    for r in reserve[:]:
        student[r-1] += 1
    
    for i in range(len(student)):
        if student[i] >= 2:
            if i >= 1 and student[i-1] == 0:
                student[i-1] += 1
                student[i] -= 1
            elif i+1 < n and student[i+1] == 0:
                student[i+1] += 1
                student[i] -= 1
    answer = Counter(student)
    return answer[1] + answer[2]

# (*)
def solution2(n, lost, reserve):
    reserveList = [r for r in reserve if r not in lost]
    lostList = [l for l in lost if l not in reserve]

    for r in reserveList:
        front = r - 1
        back = r + 1
        if front in lostList:
            lostList.remove(front)
        elif back in lostList:
            lostList.remove(back)
    return n - len(lostList)

n = 5
lost = [2, 4]
reserve = [1, 3, 5]
print(solution2(n, lost, reserve))