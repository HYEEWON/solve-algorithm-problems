import sys

n = int(sys.stdin.readline().strip())
stairs = [0 for i in range(n+1)]
answer = [0 for i in range(n+1)]

for i in range(1, n+1):
    stairs[i] = int(sys.stdin.readline().strip())

print(stairs)

answer[1] = stairs[1]
if n > 1:
    answer[2] = stairs[1]+stairs[2]

for i in range(3, n+1):
    answer[i] = max(answer[i-2]+ stairs[i], answer[i-3]+stairs[i-1]+stairs[i])

sys.stdout.write(str(answer[n]))