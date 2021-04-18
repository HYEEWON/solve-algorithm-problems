import sys

N = int(sys.stdin.readline())
weights = list(map(int, sys.stdin.readline().strip().split()))
weights.sort()

answer = 1
for w in weights:
    if answer >= w:
        answer += w
    else:
        break

sys.stdout.write(str(answer))