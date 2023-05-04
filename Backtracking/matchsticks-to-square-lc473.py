# page 68

from typing import List
"""
The only possible square side length = sum(matchsticks)/4 and if this isn't an integer - you can straight up return False. 

"""


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        sumSticks = sum(matchsticks)

        if sumSticks % 4 != 0 or len(matchsticks) < 4:
            return False

        # important piece of optimization!
        matchsticks.sort(reverse=True)

        sideLength = sumSticks // 4
        sides = [sideLength] * 4

        def backtrack(start, sides):

            if start == len(matchsticks):
                return True

            for i in range(4):
                if sides[i] >= matchsticks[start]:
                    sides[i] -= matchsticks[start]

                    if backtrack(start + 1, sides):
                        return True

                    sides[i] += matchsticks[start]

            return False

        return backtrack(0, sides)



