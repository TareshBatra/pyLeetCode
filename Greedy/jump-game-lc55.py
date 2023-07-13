from typing import List

# Time: O(n)
# Space: O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # leastPossibleInd is to keep track of the smallest index in the array from which we can reach the last index
        leastPossibleInd = len(nums) - 1  # initially, we can reach the last index from the last index itself

        # iterating in reverse order to keep updating the leastPossibleInd
        for i in range(len(nums) - 2, -1, -1):
            # if the leastPossibleInd can be reached from the current index, update the leastPossibleInd
            if i + nums[i] >= leastPossibleInd:
                leastPossibleInd = i

        return leastPossibleInd == 0  # if the leastPossibleInd is 0, we can reach the last index from the first index
