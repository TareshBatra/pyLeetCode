# page 54
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# recursive DFS

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.result = 0

        def dfs(node, maxVal):

            if node.left:
                dfs(node.left, max(maxVal, node.left.val))

            if node.right:
                dfs(node.right, max(maxVal, node.right.val))

            if node.val >= maxVal:
                self.result += 1

            return

        dfs(root, root.val)
        return self.result
