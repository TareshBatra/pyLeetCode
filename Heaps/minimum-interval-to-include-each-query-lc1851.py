from typing import List
import heapq

# The idea is to read the queries in sorted order and maintain a min heap (min over the interval size) of the intervals
# whose lower limit is less than or equal to the current query and whose upper limit is greater than or equal to the
# current query. The top of the heap will be the smallest interval that contains the current query.
# The top of the heap will be the smallest interval that contains the current query.
# If corresponding to a query, there are no intervals in the heap, then the answer is -1.

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        result = {}
        intervalHeap = []
        i = 0

        for q in sorted(queries):

            if q in result:
                continue

            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(intervalHeap, (r - l + 1, r))
                i += 1

            while intervalHeap and intervalHeap[0][1] < q:
                heapq.heappop(intervalHeap)

            result[q] = intervalHeap[0][0] if intervalHeap else -1

        return [result[q] for q in queries]



