# page 78
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        self.memo = {}

        def func(start):
            if start == len(nums):
                return 0

            elif start in self.memo:
                return self.memo[start]

            else:

                result = 1

                for i in range(start, len(nums)):
                    if nums[i] > nums[start]:
                        result = max(result, 1 + func(i))

                self.memo[start] = result
                return self.memo[start]

        answer = 0

        for i in range(len(nums) - 1, -1, -1):
            answer = max(answer, func(i))

        return answer
