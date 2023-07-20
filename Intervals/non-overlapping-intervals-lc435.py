from typing import List


# Time Complexity: O(nlogn)
# Space Complexity: O(1)

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        result = 0
        intervals.sort()  # to make sure that the intervals are sorted by the start time

        prevInterval = intervals[0]

        for i, interval in enumerate(intervals[1:]):

            if prevInterval[1] <= interval[0]:  # if the previous and current intervals are non-overlapping or touching
                prevInterval = interval

            # if the prevInterval completely overlaps the present interval
            # we need to remove the prevInterval and replace it with the current interval
            # so that we can accommodate more intervals
            elif prevInterval[1] >= interval[1]:
                result += 1
                prevInterval = interval

            # if prevInterval partially overlaps the current interval.
            # we need to remove the interval with the larger end time, i.e., the current interval
            # so that we can accommodate more intervals
            else:
                result += 1

        return result
