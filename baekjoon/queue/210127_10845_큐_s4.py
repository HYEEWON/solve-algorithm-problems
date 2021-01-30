from collections import deque
import sys

N = int(sys.stdin.readline())
dq = deque()

for n in range(N):
    op = sys.stdin.readline().split()
    if op[0] == "push":
        dq.append(op[1])
    elif op[0] == "pop":
        if len(dq) == 0: 
            sys.stdout.write(str(-1)+'\n')
        else:
            sys.stdout.write(str(dq.popleft())+'\n')
    elif op[0] == "size":
        sys.stdout.write(str(len(dq))+'\n')
    elif op[0] == "empty":
        if len(dq) == 0: 
            sys.stdout.write(str(1)+'\n')
        else:
            sys.stdout.write(str(0)+'\n')
    elif op[0] == "front":
        if len(dq) == 0: 
            sys.stdout.write(str(-1)+'\n')
        else:
            sys.stdout.write(str(dq[0])+'\n')
    elif op[0] == "back":
        if len(dq) == 0: 
            sys.stdout.write(str(-1)+'\n')
        else:
            sys.stdout.write(str(dq[-1])+'\n')