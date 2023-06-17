# page 83

from typing import List

'''
S (Subproblem) - uniqueChillar(i,target) is the number of unique ways to create the target amount using coins starting from the ith index in the list
R (Relate) - uniqueChillar(i,target)= uniqueChillar(i,target - coins[i]) + uniqueChillar(i+1, target)

When you draw the recursion tree for this example, every branch should be made such that, the ith branch of the root node uses coins in the subarray coins[i:] to create the target. Subsequently, the daughter nodes should follow their respective branches, Thus these 2 cases. For every node, we have to explore 2 examples:

1. with at least 1 coin of the current denomination, thus in general choose from coins[i:], aiming to find target - coins[i]
2. with coins starting from the next index, thus excluding the current denomination and choosing from coins[i+1:], aiming to find target

T (Topological Order) - 2D order, for i - descending in indices. for target - ascending in amount, starting from 0
B (Base) - uniqueChillar(i,0) = 1. uniqueChillar(>=len(coins), target) = 0. uniqueChillar(i, < 0) = 0.
O (Original Problem) - uniqueChillar(0,amount)
T (Time) - O(mn), m being the number of coin denominations and n being the amount (sum over the non-recursive work done by every sub-problem)

'''


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo_coins = {}

        def uniqueChillar(i, target):
            if (i, target) in memo_coins:
                return memo_coins[(i, target)]

            elif target == 0:
                return 1

            elif target < 0:
                return 0

            elif i >= len(coins):
                return 0

            else:
                memo_coins[(i, target)] = uniqueChillar(i, target - coins[i]) + uniqueChillar(i + 1, target)

                return memo_coins[(i, target)]

        return uniqueChillar(0, amount)
