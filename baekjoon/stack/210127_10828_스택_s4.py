from collections import deque
import sys

N = int(sys.stdin.readline())
st = deque()

for n in range(N):
    op = sys.stdin.readline().split()
    if op[0] == "push":
        st.appendleft(op[1])
    elif op[0] == "pop":
        if len(st) == 0: 
            sys.stdout.write(str(-1)+'\n')
        else:
            sys.stdout.write(str(st.popleft())+'\n')
    elif op[0] == "size":
        sys.stdout.write(str(len(st))+'\n')
    elif op[0] == "empty":
        if len(st) == 0: 
            sys.stdout.write(str(1)+'\n')
        else:
            sys.stdout.write(str(0)+'\n')
    elif op[0] == "top":
        if len(st) == 0: 
            sys.stdout.write(str(-1)+'\n')
        else:
            sys.stdout.write(str(st[0])+'\n')