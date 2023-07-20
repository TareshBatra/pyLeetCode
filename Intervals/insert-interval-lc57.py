from typing import List


# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                result.append(newInterval)

                return result + intervals[i:]

            elif newInterval[0] > interval[1]:
                result.append(interval)

            else:
                # merging the overlapping intervals, to create an updated newInterval, which can then be inserted
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        result.append(newInterval)

        return result
