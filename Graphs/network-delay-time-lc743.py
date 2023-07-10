# page 103

from collections import defaultdict
from typing import List
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)

        for u, v, w in times:
            adjList[u].append([v, w])

        minHeap = [[0, k]]
        visited = set()

        time = 0

        # Once we have hit all the nodes, we need not continue
        while minHeap and len(visited) < n:

            t, node = heapq.heappop(minHeap)

            if node in visited:
                continue

            visited.add(node)
            time = t

            # if the node we land on does not have any outgoing edges, we must look elsewhere
            if node not in adjList:
                continue

            for v, w in adjList[node]:
                if v in visited:
                    continue

                heapq.heappush(minHeap, [t + w, v])

        if len(visited) == n:
            return time

        return -1
