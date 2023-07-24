# page 59

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        self.serialized = []

        def dfs(node):
            if not node:
                self.serialized.append('#') # to identify leaf nodes
                return

            self.serialized.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return ','.join(self.serialized)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        data = data.split(',')
        self.iterator = 0

        def dfs():
            if data[self.iterator] == '#':
                self.iterator += 1
                return None

            node = TreeNode(int(data[self.iterator]))
            self.iterator += 1

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
