# page 4

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}

        for i, num in enumerate(nums):
            res = target - num
            if res in numsDict:
                return [i, numsDict[res]]
            numsDict[num] = i
