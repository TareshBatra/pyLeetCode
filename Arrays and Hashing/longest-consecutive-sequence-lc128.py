# page 7

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numsDict = {}

        for num in nums:
            if num in numsDict:
                continue
            numsDict[num] = 1

        result = 1

        if len(nums) == 0:
            return 0

        for num in numsDict:
            if numsDict[num] == 0:
                continue

            localMax = 1
            numsDict[num] = 0
            i = 1

            while num - i in numsDict:
                localMax += 1
                numsDict[num - i] = 0
                i += 1

            i = 1

            while num + i in numsDict:
                localMax += 1
                numsDict[num + i] = 0
                i += 1

            result = max(localMax, result)

        return result
