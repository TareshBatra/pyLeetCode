# page 76

from typing import List

'''

Doesn't even seem like a dp problem. The idea here is fairly elementary. 
We are keeping track of 3 values as we move over the array: 
currMax(i) - The maximum subarray product that can be obtained using the ith element.
currMin(i) - The minimum subarray product that can be obtained using the ith element.
ansMax(i) - The maximum subarray product until the ith element. 

The reason for maintaining the currMax and currMin values is fairly simple, i.e., to accomodate negative values.

'''


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ansMax = max(nums)
        currMax = 1
        currMin = 1

        for n in nums:
            if n == 0:
                currMax = 1
                currMin = 1
            else:
                tempMax = currMax
                currMax = max(currMax * n, currMin * n, n)
                currMin = min(tempMax * n, currMin * n, n)
                ansMax = max(ansMax, currMax)

        return ansMax
