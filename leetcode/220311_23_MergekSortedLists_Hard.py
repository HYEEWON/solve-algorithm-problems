# Linked List, Heap(Priority Queue), Divide and Conquer, Merge Sort

import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
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

    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        answer = pointer = ListNode()
        cnt_none = 0

        for i in range(len(lists)):
            if not lists[i] or lists[i] == []:
                continue
            heapq.heappush(heap, (lists[i].val, i, lists[i]))

        if not heap:
            return None
        len_heap = len(heap)

        while heap:
            idx, node = heapq.heappop(heap)[1:]
            if node.next == None:
                cnt_none += 1

            pointer.val = node.val
            if cnt_none < len_heap:
                pointer.next = ListNode()
                pointer = pointer.next

            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
        return answer
