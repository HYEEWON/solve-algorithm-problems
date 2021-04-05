import sys

N = int(sys.stdin.readline())

ropes = []
for i in range(N):
    ropes.append(int(sys.stdin.readline()))

ropes.sort(reverse=True)

for i in range(N):
    ropes[i] = ropes[i]*(i+1)

sys.stdout.write(str(max(ropes)))