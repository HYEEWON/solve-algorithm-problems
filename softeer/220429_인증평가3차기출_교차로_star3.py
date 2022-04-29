import sys
import heapq

N = int(sys.stdin.readline())
road = []

for i in range(N):
    t, w = map(str, sys.stdin.readline().strip().split())
    road.append([int(t), w])

priority = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
right = {0: 3, 1: 0, 2: 1, 3: 2}
answer = [-1 for j in range(N)]
t, i, heap = 0, 0, [[], [], [], []]

while True:
    if not heap[0] and not heap[1] and not heap[2] and not heap[3] and i < N and t <= road[i][0]:
        t = road[i][0]

    while i < N and t == road[i][0]:
        heapq.heappush(heap[priority[road[i][1]]], i)
        i += 1

    if heap[0] and heap[1] and heap[2] and heap[3]:  # 교착상태
        break

    out_flag = {0: False, 1: False, 2: False, 3: False}
    out = []
    for pr, h in enumerate(heap):
        if not h:
            continue
        if not out_flag[pr] and not heap[right[pr]]:
            out_flag[pr] = True
            answer[h[0]] = t
            out.append(pr)

    if not out:
        break

    for pr in out:
        heapq.heappop(heap[pr])
    t += 1

for a in answer:
    sys.stdout.write(str(a) + '\n')