# page 97

from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parent, rank = [], []

        for i in range(len(edges) + 1):
            parent.append(i)
            rank.append(1)

        def find(node):
            p = parent[node]
            while p != parent[p]:
                # p = parent[p]
                p = parent[parent[p]]  # path compression/reduction to arrive at the answer faster

            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            elif rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]

            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
