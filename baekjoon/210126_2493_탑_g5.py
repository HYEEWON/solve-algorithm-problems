from collections import deque
import sys

N = int(input())
tops = list(map(int, input().split()))

stack = deque([[tops[0], 0]])
answer = [0 for i in range(len(tops))]

i = 1
while stack and i<N:
    top, idx = stack.popleft()
    if (tops[i] > top):
        if len(stack): 
            continue
        answer[i] = 0
        stack.appendleft([tops[i], i])
    elif (tops[i] == top):
        answer[i] = idx+1
        stack.appendleft([tops[i], i])
    else:
        answer[i] = idx+1
        stack.appendleft([top, idx])
        stack.appendleft([tops[i], i])
    i+=1
    
for ans in answer:
    sys.stdout.write(str(ans)+' ')