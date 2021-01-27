import heapq

K, N = map(int, input().split())
numbers = list(map(int, input().split()))

heap = []
for i in range(K):
    heapq.heappush(heap, numbers[i])

for i in range(N): # N번째 수
    n = heapq.heappop(heap)
    if (i == N-1):
        print(n)
        break
    for j in range(K):
        tmp = n * numbers[j]
        heapq.heappush(heap, tmp)
        if n % numbers[j] == 0:
            break
    

#(*) 참고한 풀이
import heapq

K, N = map(int, input().split())
prime = list(map(int, input().split()))
pq = []  # 곱한 값이 들어갈 리스트 (우선순위 큐)
for num in prime:
    heapq.heappush(pq, num)
for i in range(N):  # 큐에서 N번 빼면 그 값이 N번째 값이다. (우선순위 큐)
    num = heapq.heappop(pq)
    for j in range(K):  # 뺸 값에 소수를 곱해서 새로운 값을 만든다.
        new_num = num * prime[j]
        print(i, j, num, new_num)
        heapq.heappush(pq, new_num)
        if num % prime[j] == 0:  # 2 X 3은 되지만 3 X 2는 안되는 느낌으로 중복제거
            break
else:
    print(num)