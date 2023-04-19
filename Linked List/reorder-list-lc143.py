# page 42

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # slow and fast pointer technique to find the midpoint of a linked list, increase fast by twice the
        # speed as slow, so that slow points to the midpoint at the end

        slow, fast = head, head.next

        # it is important to check for both fast and fast.next because fast gets updated as fast.next.next
        # so unless fast.next exists, there will be an error in updating fast to fast.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half which starts at the node next to slow

        prev, curr = None, slow.next
        while curr:
            temp_ptr = curr.next
            curr.next = prev
            prev = curr
            curr = temp_ptr

        slow.next = None  # denotes the last node of the linked list

        # merge the two linked lists to re-order

        head1, head2 = head, prev
        while head2:
            temp_ptr = head1.next
            head1.next = head2
            head1 = head2
            head2 = temp_ptr
