# page 5

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        numsDict = {}

        for num in nums:
            if num in numsDict:
                numsDict[num] += 1
            else:
                numsDict[num] = 1

        bucketArray = [[] for i in range(len(nums) + 1)]

        for num, c in numsDict.items():
            bucketArray[c].append(num)

        result = []

        for x in reversed(bucketArray):
            if len(result) < k:
                result.extend(x)
            else:
                return result[:k + 1]
