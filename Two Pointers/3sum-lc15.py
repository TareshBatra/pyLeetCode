# page 10

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = set()
        # to save on space complexity, we have created a set to avoid duplicates but later converted it into a list

        nums = sorted(nums)

        for i, num in enumerate(nums):
            # in a sorted array once we start getting positive numbers, values succeeding it will also be positive,
            # so no way to get 0

            if num > 0:
                break

            # again, if the value is being repeated, all possible triplets have already been considered.
            elif i > 0 and num == nums[i - 1]:
                continue

            start, end = i + 1, len(nums) - 1

            while start < end:
                sum = nums[start] + nums[end] + num
                if sum == 0:
                    if (num, nums[start], nums[end]) not in result:
                        result.add((num, nums[start], nums[end]))
                    start += 1
                    end -= 1
                elif sum < 0:
                    start += 1
                else:
                    end -= 1

        return list(result)
