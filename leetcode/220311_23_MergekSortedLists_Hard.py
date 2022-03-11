# Linked List, Heap(Priority Queue), Divide and Conquer, Merge Sort

import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "listnode(" + str(self.val) + ", "+ str(self.next) + ")"

class Solution:
    def mergeKLists(self, lists):
        heap = []
        answer = pointer = ListNode()

        for i in range(len(lists)):
            if not lists[i]:
                continue
            heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            idx, node = heapq.heappop(heap)[1:]
            pointer.next = ListNode(node.val)
            pointer = pointer.next

            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
        return answer.next
