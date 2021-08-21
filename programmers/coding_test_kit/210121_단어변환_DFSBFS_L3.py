from collections import deque #BFS
def solution(begin, target, words):
    if target not in words:
        return 0
    dq = deque()
    dq.append([begin, 0])
    
    while dq:
        word, cnt = dq.popleft()
        if word == target:
            return cnt
        for i in range(len(words)):
            for idx in range(len(word)):
                if word[idx] != words[i][idx] and word[:idx] == words[i][:idx] and word[idx+1:] == words[i][idx+1:]:
                    dq.append([words[i], cnt+1])
    return 0

# DFS: 시간 초과로 안됨
import sys
sys.setrecursionlimit(10**9)
answer = -1
def dfs(word, cnt, words, target):
    if word == target:
        if answer < 0:
            answer = cnt
        else:
            answer = min(answer, cnt)
        return;

    for i in range(len(words)):
        for idx in range(len(word)):
            if word[idx] != words[i][idx] and word[:idx] == words[i][:idx] and word[idx+1:] == words[i][idx+1:]:
                dfs(words[i], cnt+1, words, target)

def solution2(begin, target, words):
    if target not in words:
        return 0
    dfs(begin, 0, words, target)
    return 0

print(solution2("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))