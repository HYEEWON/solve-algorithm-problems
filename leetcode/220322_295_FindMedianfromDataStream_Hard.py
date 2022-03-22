# Heap

# 참고하면 좋을 코드
# https://leetcode.com/problems/find-median-from-data-stream/discuss/677080/Well-commented-python-code

import heapq

class MedianFinder:
    def __init__(self):
        self.max_heap = []  # 큰 값 pop (중간보다 작은 값)
        self.min_heap = []  # 작은 값 pop (중간 ~ 큰 값)

    def addNum(self, num: int) -> None:
        if not self.max_heap:
            heapq.heappush(self.max_heap, (-num, num))
        elif len(self.min_heap) > len(self.max_heap):
            p, n = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, (-p, n))
            heapq.heappush(self.min_heap, (num, num))
        else:
            heapq.heappush(self.min_heap, (num, num))

        if self.min_heap and self.min_heap[0][1] < self.max_heap[0][1]:
            p1, n1 = heapq.heappop(self.min_heap)
            p2, n2 = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, (-p2, n2))
            heapq.heappush(self.max_heap, (-p1, n1))

    def findMedian(self) -> float:
        if not self.min_heap:
            return self.max_heap[0][1]
        elif (len(self.max_heap) + len(self.min_heap)) % 2 == 0:  # 짝수개
            return (self.min_heap[0][1] + self.max_heap[0][1]) / 2
        else:  # 홀수개
            return self.min_heap[0][1]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()