# page 74
from typing import List

'''
S (Subproblem) - Suffix, robMax(i) is the max loot that can be collection from houses starting at the house at index i
R (Relate) - robMax(i) = max(robMax(i+2)+nums[i],robMax(i+1))
Either rob the current (ith) house and then do what's best starting from house at the (i+2)th house or do not rob house i and do what's best starting from the (i+1)th house
T (Topological Order) - descending order (Suffix) 
B (Base) - climb(n), robMax(>=n) = 0
O (Original Problem) - robMax(0)
T (Time) - O(n) (sum over the non-recursive work done by every sub-problem)

'''


class Solution:
    def rob(self, nums: List[int]) -> int:
        self.memo = {}

        def robMax(i):
            if i in self.memo:
                return self.memo[i]
            elif i >= len(nums):
                return 0
            else:
                self.memo[i] = max(robMax(i + 2) + nums[i], robMax(i + 1))
                return self.memo[i]

        return robMax(0)
