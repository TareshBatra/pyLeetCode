# page 52
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# naive solution

"""
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node:
                if self.isSameTree(node,subRoot):
                    return True

                queue.append(node.left)
                queue.append(node.right)

        return False

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        queue_p = deque([p])
        queue_q = deque([q])

        while queue_p and queue_q:

            node_p = queue_p.popleft()
            node_q = queue_q.popleft()

            if node_p and node_q:

                if node_p.val != node_q.val:
                    return False

                queue_p.append(node_p.left)
                queue_p.append(node_p.right)
                queue_q.append(node_q.left)
                queue_q.append(node_q.right)

            elif node_p != node_q:
                return False

        return True
"""


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def merkle(node):
            if not node:
                return '#'
            m_left = str(merkle(node.left))
            m_right = str(merkle(node.right))
            node.merkle = hash(m_left + str(node.val) + m_right)
            return node.merkle

        merkle(root)
        merkle(subRoot)

        # dfs
        stack = [root]
        while stack:
            node = stack.pop()

            if node:
                if node.merkle == subRoot.merkle:
                    return True

                stack.extend([node.right, node.left])

        return False
