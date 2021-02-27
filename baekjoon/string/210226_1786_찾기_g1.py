import sys

T = sys.stdin.readline()[:-1]
P = sys.stdin.readline()[:-1]

pi = [0] * len(P)
j = 0
for i in range(1, len(P)):
    while j>0 and P[i] != P[j]:
        j = pi[j-1]
    if P[i] == P[j]:
        j += 1
        pi[i] = j

j = 0
answer = 0
answer2 = []
for i in range(len(T)):
    while j>0 and T[i] != P[j]:
        j = pi[j-1]
    if T[i] == P[j]:
        j += 1
        if j == len(P): 
            answer += 1
            answer2.append(i-len(P)+2)
            j = pi[j-1]

sys.stdout.write(str(answer)+'\n')
for ans in answer2:
    sys.stdout.write(str(ans)+' ')