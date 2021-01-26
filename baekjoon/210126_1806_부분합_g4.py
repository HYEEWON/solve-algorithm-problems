import sys

N, S = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

answer = N+2
low = 0
hi = 1
tmp = array[0]

while low<N:
    if hi >= N and tmp < S:
            break
    elif tmp < S:
        tmp += array[hi]
        hi += 1        
    elif tmp >= S:
        tmp -= array[low]
        low += 1
        if tmp < S:
            answer = min(answer, hi-low+1)

if answer>N:
    sys.stdout.write(str(0))
else:            
    sys.stdout.write(str(answer))

'''N, S = map(int, input().split())
array = list(map(int, input().split()))

answer = N
sums = [0]*(N+1)
for i in range(1, len(array)):
    sums[i] = sums[i-1]+array[i-1]

for i in range(N):
    for j in range(i+1, N+1):
        if sums[j] < S:
            pass
        elif sums[j]-sums[i] == S:
            answer = min(answer, j-i)
        elif sums[j]-sums[i] > S:
            break

print(answer)'''