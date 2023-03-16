# page 33

import math
from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = max(piles)

        def checkIfPossible(speed):
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / speed)

            if hours <= h:
                return True

            else:
                return False

        while l <= r:
            mid = l + (r - l) // 2

            if checkIfPossible(mid):
                ans = mid
                r = mid - 1

            else:
                l = mid + 1

        return ans
