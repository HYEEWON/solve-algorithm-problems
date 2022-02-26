from itertools import permutations

answer = 0
tmp = 0

def dfs(idx, N, k, dungeons, p):
    global tmp

    if idx == N:
        return

    if k >= dungeons[p[idx]][0]:
        k -= dungeons[p[idx]][1]
        tmp += 1

    dfs(idx+1, N, k, dungeons, p)


def solution(k, dungeons):
    global answer, tmp

    per = list(permutations([i for i in range(len(dungeons))], len(dungeons)))

    for p in per:
        tmp = 0
        dfs(0, len(dungeons), k, dungeons, p)
        answer = max(answer, tmp)
    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))