# page 57
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        stack = [root]
        self.sum = 0
        self.root2leaf = 0

        def dfs(node):

            self.root2leaf = self.root2leaf * 10 + node.val

            if not (node.left or node.right):  # identifying a leaf
                self.sum += self.root2leaf
                return

            if node.left:
                dfs(node.left)
                self.root2leaf = self.root2leaf // 10  # removing the node added

            if node.right:
                dfs(node.right)
                self.root2leaf = self.root2leaf // 10  # removing the node added

            return

        dfs(root)
        return self.sum
