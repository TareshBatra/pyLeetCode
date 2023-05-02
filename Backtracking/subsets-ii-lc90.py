# page 64

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.result = []
        self.currSubset = []

        def backtrack(start):

            self.result.append(self.currSubset.copy())

            i = start

            while i < len(nums):

                self.currSubset.append(nums[i])
                backtrack(i + 1)

                while i < len(nums) - 1 and nums[i] == nums[i + 1]:  # repetition
                    i += 1

                self.currSubset.pop()
                i += 1

            # same thing but using a for loop instead:

            """
            for i in range(start,len(nums)):
                if i > start and nums[i] == nums[i-1]: # repitition
                    continue                

                self.currSubset.append(nums[i])
                backtrack(i+1)
                self.currSubset.pop()
            """

        backtrack(0)
        return self.result
