# page 42

from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# Using a Dictionary

"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyDict = {None:None}

        curr = head

        # creating n nodes corresponding to the given linked list

        while curr:
            copy = Node(curr.val)
            copyDict[curr] = copy
            curr = curr.next

        curr = head

        while curr:

            copyDict[curr].next = copyDict[curr.next]
            copyDict[curr].random = copyDict[curr.random]

            curr = curr.next

        return copyDict[head]
"""


# interweaving the 2 lists
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        curr = head

        # creating n nodes corresponding to the given linked list

        # creating a chain of og and copied nodes

        while curr:
            temp_ptr = curr.next
            copy = Node(curr.val, curr.next, curr.random)
            curr.next = copy
            curr = temp_ptr

        copyHead = Node(0)
        curr, copy_curr = head, copyHead

        while curr:
            copy_curr.next = curr.next

            copy_curr = copy_curr.next

            copy_curr.random = curr.random.next if curr.random else None

            curr = curr.next.next

        return copyHead.next
