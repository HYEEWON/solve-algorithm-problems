# 확률, 조합

# 내 풀이
# (전체에서 1개 돌을 뽑는 확률 * (전체-1)에서 1개 돌을 뽑는 확률)을 모두 더함

# 파스칼의 삼각형을 이용할 수도 있음 (조합)
# (같은 돌에서 K개 뽑는 경우의 수) / (전체 돌에서 K개 뽑는 경우의 수)

import sys

M = int(sys.stdin.readline())
color = list(map(int, sys.stdin.readline().strip().split()))
K = int(sys.stdin.readline())

total = sum(color)
answer = 0
for c in color:
    tmp = 1
    for k in range(K):
        tmp *= ((c-k)/(total-k))
    answer += tmp
print(answer)