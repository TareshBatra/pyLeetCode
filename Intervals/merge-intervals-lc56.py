from typing import List

# Time Complexity: O(nlogn)
# Space Complexity: O(n)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        result = []
        intervals.sort() # to make sure that the intervals are sorted by the start time

        prevInterval = intervals[0]

        # Just a slight modification of the insert interval problem
        for i, interval in enumerate(intervals[1:]):

            if prevInterval[1] < interval[0]:
                result.append(prevInterval)
                prevInterval = interval

            else:
                prevInterval[0] = min(prevInterval[0], interval[0])
                prevInterval[1] = max(prevInterval[1], interval[1])

        result.append(prevInterval)
        return result
