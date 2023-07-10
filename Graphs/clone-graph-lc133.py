# page 92

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        nodesDict = {}

        def dfs(oldNode):
            if oldNode in nodesDict:
                return

            else:
                copyNode = Node(oldNode.val)
                nodesDict[oldNode] = copyNode

                for nghb in oldNode.neighbors:
                    dfs(nghb)
                    copyNode.neighbors.append(nodesDict[nghb])

        if node:
            dfs(node)
            return nodesDict[node]

        return None
