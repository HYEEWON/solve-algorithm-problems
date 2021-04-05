import sys
# 음수, 0 은 안묵는게 낫지

N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for i in range(N)]

neg, pos = [], []
answer = 0

for n in numbers:
    if n <= 0:
        neg.append(n)
    elif n == 1:
        answer += 1
    else:
        pos.append(n)

pos.sort(reverse=True)
neg.sort()       

for i in range(0, len(pos), 2):
    if i < len(pos) - 1:
        answer += pos[i]*pos[i+1]
    else:
        answer += pos[i]

for i in range(0, len(neg), 2):
    if i < len(neg) - 1:
        answer += neg[i]*neg[i+1]
    else:
        answer += neg[i]

sys.stdout.write(str(answer))