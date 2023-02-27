# page 10

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        start, end = 0, len(height) - 1
        minPointer = start if height[start] < height[end] else end
        area = height[minPointer] * (end - start)

        while start < end:
            # we are only concerned with the min pointer
            # it is important to update the minPointers each time we update start/end

            if minPointer == start:
                start += 1
                minPointer = start if height[start] < height[end] else end
                area = max(area, height[minPointer] * (end - start))

            if minPointer == end:
                end -= 1
                minPointer = start if height[start] < height[end] else end
                area = max(area, height[minPointer] * (end - start))

        return area
