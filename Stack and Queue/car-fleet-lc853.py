# page 24

from typing import List

# sorting + array

"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        positionSpeed = [(target-p,s) for p,s in zip(position,speed)]
        positionSpeed.sort()
        timeArray = []
        result = 1 # since len(position) >= 1
        fleetPointer = 0

        for gap, s in positionSpeed:
            timeArray.append(gap/s)

        for i,time in enumerate(timeArray):
            if time > timeArray[fleetPointer]:
                result += 1
                fleetPointer = i

        return result
"""


# sorting + stack

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        positionSpeed = [(target - p, s) for p, s in zip(position, speed)]
        positionSpeed.sort()

        stack = []
        for gap, s in positionSpeed:
            time = gap / s
            if stack:
                if time > stack[-1]:
                    stack.append(time)

            else:
                stack.append(time)

        return len(stack)
