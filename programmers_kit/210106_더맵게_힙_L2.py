import heapq # 이진 트리 기반의 최소 힙
# 리스트를 힙처럼 사용
def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while len(scoville) > 1:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new = first + second*2
        heapq.heappush(scoville, new)
        answer += 1
        if scoville[0] >= K:
            return answer
    return -1

scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))