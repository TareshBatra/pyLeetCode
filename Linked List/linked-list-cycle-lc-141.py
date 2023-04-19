# page 43

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Using a hash map
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = {}

        curr = head

        while curr:
            if curr in visited:
                return True

            else:
                visited[curr] = True

            curr = curr.next

        return False
"""


# using slow and fast pointers - Floyd's Hare and Tortoise Algorithm
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow, fast = head, head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
