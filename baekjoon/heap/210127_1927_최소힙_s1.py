import heapq
import sys

N = int(sys.stdin.readline().strip())
heap = []
for i in range(N):
    x = int(sys.stdin.readline().strip())
    if x > 0:
        heapq.heappush(heap, x)
    elif x == 0:
        if len(heap) > 0:
            sys.stdout.write(str(heapq.heappop(heap))+'\n')
        else:
            sys.stdout.write(str(0)+'\n')