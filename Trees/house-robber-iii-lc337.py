# page 57

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
The choice is between choosing Now or Choosing Later. The thief can either rob this node and not touch 
it's immediate children or he can skip the current node and explore the subsequent nodes with a similar dilemma. 
This problem screams DFS! The tricky bit is the sort of 2D apporach to this problem.
"""


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0)

            left = dfs(node.left)
            right = dfs(node.right)

            chooseNow = node.val + left[1] + right[1]
            chooseLater = max(left) + max(right)

            return (chooseNow, chooseLater)

        return max(dfs(root))
