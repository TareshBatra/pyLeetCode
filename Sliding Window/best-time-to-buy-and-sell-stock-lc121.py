# page 14

from typing import List

# wrong solution-
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, len(prices) - 1
        result = 0

        for i in range(len(prices)):
            if prices[i] <= prices[buy]:
                buy = i
                if buy >= sell:
                    break
                result = max(prices[sell]-prices[buy], result)

            if prices[len(prices) - 1 - i] >= prices[sell]:
                sell = len(prices) - 1 - i
                if buy >= sell:
                    break
                result = max(prices[sell]-prices[buy], result)

        return result
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        result = 0

        for price in prices:
            if price > smallest:
                result = max(result, price - smallest)
            else:
                smallest = price

        return result
