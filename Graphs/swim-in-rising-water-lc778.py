# page 104

from typing import List
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()

        time = 0

        minHeap = [[0, (0, 0)]] # [time taken to reach the point (r,c), (r,c)]

        while minHeap:
            t, (r, c) = heapq.heappop(minHeap)

            if (r, c) in visited:
                continue

            t = max(t, grid[r][c])
            # time >= the elevation of the point from which you have to swim (t, i.e., height of water)

            visited.add((r, c))
            time = t

            if (r, c) == (n - 1, n - 1):
                return time

            LRTB = [[-1, 0], [1, 0], [0, -1], [0, 1]]

            for dr in LRTB:
                row, col = r + dr[0], c + dr[1]

                if row in range(n) and col in range(n) and (row, col) not in visited:
                    heapq.heappush(minHeap, [max(time, grid[row][col]), (row, col)])

                    # time >= the elevation of the point to which you have to swim (t, i.e., height of water)


        return -1
