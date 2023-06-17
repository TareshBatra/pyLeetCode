# page 82

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.memo = {}

        def dp(i, canBuy, canSell):
            if (i, canBuy, canSell) in self.memo.keys():
                return self.memo[(i, canBuy, canSell)]

            elif i >= len(prices):
                return 0

            else:
                if canBuy:
                    self.memo[(i, canBuy, canSell)] = max(dp(i + 1, False, True) - prices[i],
                                                          dp(i + 1, True, False))  # Choosing between buy and cooldown
                    return self.memo[(i, canBuy, canSell)]

                elif canSell:
                    self.memo[(i, canBuy, canSell)] = max(dp(i + 1, False, False) + prices[i],
                                                          dp(i + 1, False, True))  # Choosing between sell and cooldown
                    return self.memo[(i, canBuy, canSell)]

                else:
                    self.memo[(i, canBuy, canSell)] = dp(i + 1, True,
                                                         False)  # Cooldown and be able to buy at the next price.
                    return self.memo[(i, canBuy, canSell)]

        return dp(0, True, False)
