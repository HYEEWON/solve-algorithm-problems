import sys

n, k = map(int, sys.stdin.readline().strip().split())

answer = []
cnt = 0
def dfs(number, sums, string):
    global n, k, cnt
    if sums == n:
        answer.append(string[:-1])
        cnt+=1
        return
    if sums > n:
        return

    for i in range(1, 4):
        dfs(i, sums+i, string+str(i)+'+')
    return 


dfs(0, 0, '')
answer.sort()
if cnt >= k:
    sys.stdout.write(answer[k-1])
else:
    sys.stdout.write(str(-1))