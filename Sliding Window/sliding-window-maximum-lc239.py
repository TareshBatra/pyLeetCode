# page 20

from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        dq = deque()  # index
        winStart, winEnd = 0, 0

        while winEnd < len(nums):
            if winEnd - winStart < k:
                if dq and dq[-1] >= nums[winEnd]:
                    dq.append(nums[winEnd])

                elif dq and dq[-1] < nums[winEnd]:
                    while dq and dq[-1] < nums[winEnd]:
                        val = dq.pop()
                    dq.append(nums[winEnd])

                else:  # for when dq is empty
                    dq.append(nums[winEnd])

                winEnd += 1

            else:
                result.append(dq[0])
                # if the first element is at the beginning, we must let it go for the subsequent windows
                if nums[winStart] == dq[0]:
                    dq.popleft()
                winStart += 1

        # for the final k sized window
        result.append(dq.popleft())

        return result
