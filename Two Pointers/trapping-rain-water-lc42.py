# page 11

from typing import List

"""
Time Limit Exceeded:

class Solution:
    def trap(self, height: List[int]) -> int:
        start, end = 0,1
        water = 0

        def calculateWaterAdded(i,j):
            minPointer = i if height[i] < height[j] else j
            waterAdded = 0
            for k in range(i+1,j):
                waterAdded += height[minPointer] - height[k]
            return waterAdded

        while start < len(height)-1:
            if end >= len(height) -1:
                break
            i = end
            while height[start] > height[i]:
                i+=1
                if i > len(height) -1:
                    break
                end = end if height[end] > height[i] else i

            water += calculateWaterAdded(start,end)
            start = end
            end = start+1

         return water

"""


class Solution:
    def trap(self, height: List[int]) -> int:

        start, end = 0, len(height) - 1
        startMax, endMax = height[0], height[len(height) - 1]
        result = 0
        while start < end:
            if startMax < endMax:
                start += 1
                startMax = max(startMax, height[start])
                result += startMax - height[start]
            else:
                end -= 1
                endMax = max(endMax, height[end])
                result += endMax - height[end]
        return result
