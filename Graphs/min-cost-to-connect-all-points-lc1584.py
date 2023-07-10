# page 102

from typing import List
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        result = 0
        visited = set()

        def manhDist(p1, p2):
            return abs(points[p1][0] - points[p2][0]) + abs(points[p1][1] - points[p2][1])

        minHeap = [[0, 0]]  # [cost, destination point]

        while len(visited) < len(points):

            cost, dstPoint = heapq.heappop(minHeap)  # popping the min cost element

            if dstPoint in visited:
                continue

            result += cost
            visited.add(dstPoint)

            for i in range(len(points)):
                if i in visited:
                    continue

                heapq.heappush(minHeap, [manhDist(dstPoint, i), i])

        return result
