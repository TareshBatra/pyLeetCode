# page 48

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        index = 1
        left, curr_node = dummy, head

        while curr_node:

            if index % k == 0:
                nextPtr = curr_node.next
                firstElement = left.next
                curr_node.next = None

                left.next = self.reverseList(left.next)
                firstElement.next = nextPtr

                left, curr_node = firstElement, nextPtr
                index += 1

            else:
                curr_node = curr_node.next
                index += 1

        return dummy.next

    def reverseList(self, head: Optional[ListNode]):
        curr_node = head
        prev_node = None

        while curr_node != None:
            # temporary pointer to the next node
            temp_ptr = curr_node.next
            # reversing the order
            curr_node.next = prev_node

            # moving the loop along by shifting the previous and current nodes
            prev_node = curr_node
            curr_node = temp_ptr

        return prev_node
