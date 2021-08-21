from collections import defaultdict

# 수정한 풀이
def solution(N, number):
    if number == N:
        return 1
    answer = defaultdict(list)
    answer[1].append(N)
    tmp = set()
    tmp.add(N)
    for cnt in range(2, 9):
        result = set()
        for c in range(1, cnt):
            for a in answer[c]:
                for b in answer[cnt-c]:
                    result.update([int(str(N)*cnt), a+b, a-b, a*b])
                    if b != 0:
                        result.add(a//b)
        for r in result:
            if r not in tmp:
                answer[cnt].append(r)
            tmp.add(r)
        if number in answer[cnt]:
            return cnt
    return -1

# 틀린 풀이    
def solution2(N, number):
    if number == N:
        return 1
    answer = defaultdict(list)
    answer[1].append(N)
    tmp = set()
    tmp.add(N)
    for cnt in range(2, 9):
        result = set()
        for ans in answer[cnt-1]:
            result.update([int(str(N)*cnt), ans+N, ans-N, ans*N, ans//N, N-ans])
            if ans != 0:
                result.add(N//ans)
        for r in result:
            if r not in tmp:
                answer[cnt].append(r)
            tmp.add(r)
        print(answer)
        if number in answer[cnt]:
            return cnt
    return -1