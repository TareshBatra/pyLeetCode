# page 91

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        visited = set()

        m, n = len(grid), len(grid[0])

        # Recursive Depth First Search

        def dfs(r, c):
            if r in range(m) and c in range(n) and grid[r][c] == '1' and (r, c) not in visited:
                visited.add((r, c))

                LRTB = [[-1, 0], [1, 0], [0, -1], [0, 1]]

                for dr in LRTB:
                    dfs(r + dr[0], c + dr[1])

            else:
                return

        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    numIslands += 1

        return numIslands


"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        visited = set()

        m, n = len(grid), len(grid[0])

        # Breadth First Search

        def bfs(r,c):
            queue = deque()
            visited.add((r,c))
            queue.append((r,c))

            while queue:
                row, col = queue.popleft()
                LRTB = [[-1,0], [1,0], [0,-1], [0,1]]

                for dr in LRTB:
                    newR, newC = row + dr[0], col + dr[1]

                    if newR in range(m) and newC in range(n) and grid[newR][newC] == '1' and (newR, newC) not in visited:
                        queue.append((newR,newC))
                        visited.add((newR,newC))


        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    numIslands += 1

        return numIslands
"""

"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        visited = set()

        m, n = len(grid), len(grid[0])

        # Iterative Depth First Search

        def dfs(r,c):
            stack = []
            visited.add((r,c))
            stack.append((r,c))

            while stack:
                row, col = stack.pop()
                LRTB = [[-1,0], [1,0], [0,-1], [0,1]]

                for dr in LRTB:
                    newR, newC = row + dr[0], col + dr[1]

                    if newR in range(m) and newC in range(n) and grid[newR][newC] == '1' and (newR, newC) not in visited:
                        stack.append((newR,newC))
                        visited.add((newR,newC))


        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1' and (r,c) not in visited:
                    dfs(r,c)
                    numIslands += 1

        return numIslands 
"""
