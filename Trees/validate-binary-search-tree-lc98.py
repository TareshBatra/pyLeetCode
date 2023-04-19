# page 54
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        self.result = True

        def dfs(node, leftVal, rightVal):

            if not node:
                return

            if not (node.val > leftVal and node.val < rightVal):
                self.result = False
                exit

            dfs(node.left, leftVal, node.val)
            dfs(node.right, node.val, rightVal)

            return

        dfs(root, float('-inf'), float('inf'))

        return self.result
