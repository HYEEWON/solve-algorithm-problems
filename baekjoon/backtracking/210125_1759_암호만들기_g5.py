# 백트랙킹

import sys

L, C = map(int, input().split())
letters = input().split()
letters.sort()

visit = [0 for i in range(C)]

def alpha(a, cnt1, cnt2):
    if a in ['a', 'e', 'i', 'o', 'u']:
        return cnt1+1, cnt2
    return cnt1, cnt2+1

def dfs(idx, cnt, cnt1, cnt2):
    if cnt == L and cnt1 >= 1 and cnt2 >= 2:
        s = ''
        for i in range(len(visit)):
            if visit[i] == 1:
                s += letters[i]
        
        sys.stdout.write(s+'\n')
        return
    for i in range(idx+1, C):
        if visit[i] == 0:
            visit[i] = 1
            c1, c2 = alpha(letters[i], cnt1, cnt2)
            dfs(i, cnt+1, c1, c2)
            visit[i] = 0


for i in range(0, C-L+1):
    visit[i] = 1
    cnt1, cnt2 = alpha(letters[i], 0, 0)
    dfs(i, 1, cnt1, cnt2)
    visit[i] = 0