# page 63

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.currSubset = []

        def backtrack(start):
            self.result.append(self.currSubset.copy())

            # copy to ensure that it does not link to the object self.currSubset.
            # If you do not use copy(), you'll get an array full of the last value taken by self.currSubset (in this case - [])

            # my solution space

            for i in range(start, len(nums)):
                # with the ith element
                self.currSubset.append(nums[i])

                backtrack(i + 1)

                # without the ith element
                self.currSubset.pop()

                """
                you could also simply just add a parameter to the func currSubset
                and write - 

                backtrack(i+1, currSubset + [nums[i]])
                """

        backtrack(0)
        return self.result


"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []

        def backtrack(start, currSubset):

            if start == len(nums):
                self.result.append(currSubset.copy())

            else:
                backtrack(start + 1, currSubset + [nums[start]])
                backtrack(start + 1, currSubset)

        backtrack(0, [])
        return self.result     
"""
