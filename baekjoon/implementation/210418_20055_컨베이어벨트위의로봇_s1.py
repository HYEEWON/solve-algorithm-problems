import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
A = deque(list(map(int, sys.stdin.readline().strip().split())))
Robot = deque([0 for i in range(len(A))])

answer = 0
while True:
    answer += 1

    Robot.appendleft(Robot.pop())
    A.appendleft(A.pop())

    if Robot[N-1] == 1:
        Robot[N-1] = 0

    for i in range(N-2, -1, -1):
        if Robot[i] == 1:
            if A[i+1] > 0 and Robot[i+1] == 0:
                Robot[i], Robot[i+1] = 0, 1
                A[i+1] -= 1

    if Robot[N-1] == 1:
        Robot[N-1] = 0

    if A[0] > 0 and Robot[0] == 0:
        A[0] -= 1
        Robot[0] = 1

    if A.count(0) >= K:
        break

sys.stdout.write(str(answer))