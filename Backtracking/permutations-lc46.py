# page 64

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []

        def backtrack(usable, path):
            if not usable:
                self.result.append(path)
                return

            else:
                for i in range(len(usable)):
                    path.append(usable[i])
                    backtrack(usable[:i] + usable[i + 1:], path)
                    path.pop()

        backtrack(nums, [])
        return self.result


# Alternate Approaches

"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []

        def backtrack(start):

            if start == len(nums):
                # print(nums)
                self.result.append(nums.copy())

            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                backtrack(start+1)
                nums[i],nums[start] = nums[start], nums[i]


        backtrack(0)
        return self.result

"""

"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        self.result = []
        self.currPerm = []
        visited = [False]*len(nums)

        def backtrack():
            if len(self.currPerm) == len(nums):
                self.result.append(self.currPerm.copy())
            else:
                for i in range(len(nums)):

                    if visited[i]:
                        continue
                    visited[i] = True
                    self.currPerm.append(nums[i])

                    backtrack()

                    self.currPerm.pop()
                    visited[i] = False

        backtrack()

        return self.result
"""
