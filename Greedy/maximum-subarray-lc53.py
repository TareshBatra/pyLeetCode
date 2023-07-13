from typing import List

# Kadane's Algorithm
# Time: O(n)
# Space: O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum, maxSum = 0, 0

        for i, num in enumerate(nums):
            # we only need to check whether adding an element to the current subarray makes sense if it is negative
            if num < 0:
                currSum = max(currSum + num, 0)  # checking if the total sum after including num is negative or not

            else:
                currSum += num
                maxSum = max(maxSum, currSum)

        if maxSum == 0:  # all negative values
            return max(nums)

        else:
            return maxSum
