# Linked List, Recursion

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        reverse_head = ListNode()
        reverse_head.val = head.val
        reverse_head.next = None

        while head.next != None:
            head.val = head.next.val
            head.next = head.next.next

            tmp_head = ListNode()
            tmp_head.val = head.val
            tmp_head.next = reverse_head

            reverse_head = tmp_head
