# page 93
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        result = []

        m, n = len(heights), len(heights[0])

        def dfs(r, c, ocean, prev):
            if ocean == "pacific":

                if r in range(m) and c in range(n) and (r, c) not in pacific and heights[r][c] >= prev:
                    pacific.add((r, c))

                    LRTB = [[-1, 0], [1, 0], [0, -1], [0, 1]]

                    for dr in LRTB:
                        dfs(r + dr[0], c + dr[1], 'pacific', heights[r][c])

            else:

                if r in range(m) and c in range(n) and (r, c) not in atlantic and heights[r][c] >= prev:
                    atlantic.add((r, c))

                    LRTB = [[-1, 0], [1, 0], [0, -1], [0, 1]]

                    for dr in LRTB:
                        dfs(r + dr[0], c + dr[1], 'atlantic', heights[r][c])

        # the heights at the border can reach their corresponding oceans
        # passing the previous height as the height of the border point to make sure that it gets added to the set
        for c in range(n):
            dfs(0, c, 'pacific', heights[0][c])
            dfs(m - 1, c, 'atlantic', heights[m - 1][c])

        for r in range(m):
            dfs(r, 0, 'pacific', heights[r][0])
            dfs(r, n - 1, 'atlantic', heights[r][n - 1])

        for r in range(m):
            for c in range(n):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result
