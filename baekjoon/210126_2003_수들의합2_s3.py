import sys

#(#) 단순한 풀이
N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

consecutiveSum = [0 for i in range(N+1)] #배열의 연속 합
for i in range(1, N+1):
    consecutiveSum[i] = consecutiveSum[i-1]+numbers[i-1]

answer = 0
for i in range(N):
    for j in range(i+1, N+1):
        if consecutiveSum[j] < M:
            pass
        elif consecutiveSum[j] - consecutiveSum[i] > M:
            break
        elif consecutiveSum[j] - consecutiveSum[i] == M:
            answer += 1
            break
    
sys.stdout.write(str(answer))


#(*) 투 포인터 풀이
import sys

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

answer = 0
low, hi = 0, 1
tmp = numbers[low]

while low<N:
    if tmp == M:
        answer += 1
        tmp -= numbers[low]
        low += 1
    if hi >= N and tmp < M:
            break
    elif tmp < M:
        tmp += numbers[hi]
        hi += 1
    elif tmp > M:
        tmp -= numbers[low]
        low += 1

sys.stdout.write(str(answer))

# 시간 초과 풀이
import sys

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

answer = 0
for i in range(N):
    for j in range(N, i, -1):
        ans = sum(numbers[i:j])
        if ans == M:
            answer+=1
        elif ans < M:
            break
sys.stdout.write(str(answer))