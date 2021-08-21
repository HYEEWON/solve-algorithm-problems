import heapq
def solution(operations):
    heap = []
    for op in operations:
        if "I" in op:
            op = op.split()
            heapq.heappush(heap, int(op[1]))
        elif len(heap) > 0:
            if "D 1" == op:
                heapq.heapify(heap)
                heap.remove(max(heap))
            elif "D -1" == op:
                heapq.heapify(heap)
                heapq.heappop(heap)
    if len(heap) == 0:
        return [0, 0]
    heapq.heapify(heap)
    return [max(heap), heap[0]]

def solution2(operations):
    maxHeap, minHeap = [], []
    for op in operations:
        if "I" in op:
            op = op.split()
            heapq.heappush(maxHeap, (-int(op[1]), int(op[1])))
            heapq.heappush(minHeap, int(op[1]))
        elif len(maxHeap) > 0:
            if "D 1" == op:
                minHeap.remove(maxHeap[0][1])
                heapq.heapify(maxHeap)
                heapq.heappop(maxHeap)
            elif "D -1" == op: #D -1
                maxHeap.remove((-minHeap[0], minHeap[0]))
                heapq.heapify(minHeap)
                heapq.heappop(minHeap)
    if len(maxHeap) == 0 or len(minHeap) == 0:
        return [0, 0]
    heapq.heapify(maxHeap)
    heapq.heapify(minHeap)
    return [maxHeap[0][1], minHeap[0]]

print(solution(["I 5","I 5","I -5","I -5", "D -1"]))
print(solution(["I 16","D 1"]))
print(solution(["I 7","I 5","I -5","D -1"]))
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
print(solution(["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]))
print(solution(["I 1", "I 2", "I 3", "I 4", "I 5", "I 6", "I 7", "I 8", "I 9", "I 10", "D 1", "D -1", "D 1", "D -1", "I 1", "I 2", "I 3", "I 4", "I 5", "I 6", "I 7", "I 8", "I 9", "I 10", "D 1", "D -1", "D 1", "D -1"]))
