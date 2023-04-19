# page 58
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = root.val

        def dfs(node):
            if not node:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            self.result = max(self.result, node.val + left + right)  # trying the path with the current node as the root

            return node.val + max(left, right)  # returning the max path value through on of the subtrees

        dfs(root)
        return self.result
