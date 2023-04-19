# page 42

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        right, left = head, head

        for _ in range(n):
            right = right.next

        if not right:
            return head.next

        while right.next:
            right, left = right.next, left.next

        left.next = left.next.next

        return head
