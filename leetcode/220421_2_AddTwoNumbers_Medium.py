# Linked List, Math, Recursion

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def dfs(self, root, n):
        n += str(root.val)
        if root.next:
            n = self.dfs(root.next, n)
        return n

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = self.dfs(l1, '')[::-1]
        n2 = self.dfs(l2, '')[::-1]
        n = str(int(n1) + int(n2))

        answer = ListNode()
        tmp = answer
        for i in range(len(n) - 1, -1, -1):
            tmp.val = n[i]
            if i == 0:
                break
            tmp.next = ListNode()
            tmp = tmp.next
        return answer

    # 참고 풀이
    # https://leetcode.com/problems/add-two-numbers/discuss/922317/Python-solution
    # Carry를 두어 역순으로 더함
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        tmp = answer
        carry = 0

        # 수의 길이가 항상 같지는 않음
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next

            if l2:
                carry += l2.val
                l2 = l2.next

            tmp.next = ListNode(carry % 10)
            carry = carry // 10
            tmp = tmp.next

        return answer.next


























