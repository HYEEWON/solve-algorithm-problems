def solution(N, stages):
    answer = [[i+1, 0] for i in range(N)]
    total = len(stages)
    for n in range(1, N+1):
        if total == 0:
            answer[n-1][1] = 0
            continue
        cnt = stages.count(n)
        answer[n-1][1] = cnt / total
        total -= cnt
    answer = sorted(answer, key=lambda x: (-x[1], x[0]))
    ret = [answer[i][0] for i in range(len(answer))]
    return ret

#(*)
def solution2(N, stages):
    answer = {}
    total = len(stages)
    for n in range(1, N+1):
        try:
            answer[n] = stages.count(n) / len([i for i in stages if i>=n])
        except:
            answer[n] = 0
    answer = sorted(answer, key=answer.get, reverse=True)
    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution2(N, stages))