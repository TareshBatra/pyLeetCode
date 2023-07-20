# page 94
from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        fresh, time = 0, 0

        queue = deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh += 1

                elif grid[r][c] == 2:
                    queue.append((r, c))

        while fresh > 0 and queue:
            l = len(queue)
            # this for loop is to make sure that time is added only once for all rotten oranges existing together.
            for i in range(l):
                row, col = queue.popleft()

                LRTB = [[-1, 0], [1, 0], [0, -1], [0, 1]]

                for dr in LRTB:
                    r, c = row + dr[0], col + dr[1]

                    if r in range(m) and c in range(n) and grid[r][c] == 1:
                        grid[r][c] = 2
                        fresh -= 1
                        queue.append((r, c))

            time += 1

        if fresh > 0:
            return -1

        return time
