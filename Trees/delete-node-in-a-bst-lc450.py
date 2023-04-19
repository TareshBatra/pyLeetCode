# page 54
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        parent = None
        curr_node = root
        found = False

        # finding the node that needs to be deleted
        while curr_node:
            if key == curr_node.val:
                found = True
                break

            parent = curr_node

            if key > curr_node.val:
                curr_node = curr_node.right

            else:
                curr_node = curr_node.left

        if not found:
            return root

        curr_left = curr_node.left
        curr_right = curr_node.right

        if parent:  # if the node to be deleted is not the root of the tree
            if curr_left and curr_right:

                if parent.left == curr_node:
                    parent.left = curr_left

                else:
                    parent.right = curr_left

                # interchanging
                temp_right = curr_left.right
                curr_left.right = curr_right

                while curr_right.left:
                    curr_right = curr_right.left

                curr_right.left = temp_right

            else:

                if parent.left == curr_node:

                    parent.left = curr_left or curr_right

                else:
                    parent.right = curr_left or curr_right

        else:  # if the node to be to deleted is the root of the tree
            if curr_left and curr_right:
                root = curr_left

                # interchanging
                temp_right = curr_left.right
                curr_left.right = curr_right

                while curr_right.left:
                    curr_right = curr_right.left

                curr_right.left = temp_right

            else:
                root = curr_left or curr_right

        return root



















