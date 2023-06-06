# page 78
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        self.memo = {}
        array_sum = sum(nums)

        def partition(i, target):

            if (i, target) in self.memo.keys():
                return self.memo[(i, target)]

            elif target == 0:
                return True

            elif i >= len(nums):
                return False

            else:
                self.memo[(i, target)] = partition(i + 1, target) or partition(i + 1, target - nums[i])
                return self.memo[(i, target)]

        if (array_sum % 2 == 0):
            return partition(0, array_sum / 2)
        else:
            return False
