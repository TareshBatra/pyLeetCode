# page 104

from collections import defaultdict, deque
from typing import List
import heapq


# BFS with a minCost List to update the minCost to reach all nodes

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)

        for frm, to, price in flights:
            adjList[frm].append([to, price])

        queue = deque()
        queue.append([src, 0])  # [node, cost of reaching the node]
        stops = 0

        minCost = []

        for i in range(n):
            if i == src:
                minCost.append(0)

            else:
                minCost.append(float('inf'))

        # bfs
        while queue and stops < k + 1:
            l = len(queue)

            for i in range(l):
                node, cost = queue.popleft()

                for n, p in adjList[node]:
                    if cost + p >= minCost[n]:
                        continue

                    else:
                        minCost[n] = cost + p
                        queue.append([n, cost + p])

            stops += 1

        if minCost[dst] == float('inf'):
            return -1

        else:
            return minCost[dst]


# Dijkstra (TLE)

"""
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)

        for frm ,to, price in flights:
            adjList[frm].append([to,price])

        minHeap = [[0,src,0]] # [cost to reach the node, node, stops required]

        while minHeap:
            cost, node, stops = heapq.heappop(minHeap)

            if stops > k+1:
                continue

            if node == dst:
                return cost

            for n,p in adjList[node]:
                heapq.heappush(minHeap,[cost + p, n, stops + 1])

        return -1
"""
