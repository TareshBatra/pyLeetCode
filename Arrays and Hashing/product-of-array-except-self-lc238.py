# page 6

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        postPro = 1
        prePro = 1

        for i, num in enumerate(nums):
            result[i] *= prePro
            result[len(nums) - 1 - i] *= postPro
            prePro *= num
            postPro *= nums[len(nums) - 1 - i]

        return result
