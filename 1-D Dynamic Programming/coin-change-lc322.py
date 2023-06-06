# page 75

from typing import List
import math

'''
S (Subproblem) - dp(target) is the minimun number of coins required to get target.
R (Relate) - dp(target) = 1 + min(dp(target-coin) for coin in coins)
T (Topological Order) - Ascending Order of amount
B (Base) - dp(0) = 0
O (Original Problem) - dp(amount)
T (Time) - O(mn), m being the number of coin denominations and n being the amount (sum over the non-recursive work done by every sub-problem)

'''


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.memo = {}
        self.memo[0] = 0
        for coin in coins:
            self.memo[coin] = 1

        def dp(target):
            if target in self.memo:
                return self.memo[target]

            elif target < 0:  # wrong path
                return float('inf')

            else:
                res = float('inf')

                for coin in coins:
                    res = min(1 + dp(target - coin), res)

                self.memo[target] = res
                return self.memo[target]

        if math.isfinite(dp(amount)):
            return dp(amount)

        else:
            return -1
