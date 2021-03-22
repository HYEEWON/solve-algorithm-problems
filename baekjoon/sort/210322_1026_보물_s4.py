import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().strip().split()))
B = list(map(int, sys.stdin.readline().strip().split()))

A.sort()
B = sorted(B, reverse=True)
answer = 0
for i in range(N):
    answer += A[i]*B[i]

# answer = sum([a*b for a, b in zip(sorted(A), sorted(B, reverse=True))])
print(answer)


