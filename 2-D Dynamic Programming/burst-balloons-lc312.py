# page 86
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        self.memo = {}

        numsModified = [1] + nums + [1]

        def dp(i, j):

            if i == j:
                return 0

            elif (i, j) in self.memo:
                return self.memo[(i, j)]

            else:
                res = 0

                for k in range(i + 1, j):
                    res = max(res, numsModified[i] * numsModified[k] * numsModified[j] + dp(i, k) + dp(k, j))

                self.memo[(i, j)] = res
                return res

        return dp(0, len(numsModified) - 1)
