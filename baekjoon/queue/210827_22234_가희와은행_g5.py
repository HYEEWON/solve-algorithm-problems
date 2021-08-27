import sys
from collections import deque

N, T, W = map(int, sys.stdin.readline().strip().split())

customers = deque()
for i in range(N):
    p, t = map(int, sys.stdin.readline().strip().split())
    customers.append([p, t, 0])

tmp_customers = []
M = int(sys.stdin.readline())
for i in range(M):
    p, t, c = map(int, sys.stdin.readline().strip().split())
    tmp_customers.append([p, t, c])
tmp_customers = deque(sorted(tmp_customers, key=lambda x:x[2]))

answer = []
w = 1
tmp_cnt = 0
while customers:
    if tmp_customers and tmp_customers[0][2] == w:
        customers.append(tmp_customers.popleft())

    sys.stdout.write(str(customers[0][0]) + '\n')

    customers[0][1] -= 1
    tmp_cnt += 1

    if customers[0][1] > 0 and tmp_cnt >= T:
        customers.append(customers.popleft())
        tmp_cnt = 0
    elif customers[0][1] == 0:
        customers.popleft()
        tmp_cnt = 0
    w += 1
    if w > W:
        break
