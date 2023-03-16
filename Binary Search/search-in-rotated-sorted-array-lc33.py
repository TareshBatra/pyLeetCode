# page 34

from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:

        def findMin():
            if nums[0] <= nums[-1]:
                return 0

            l, h = 0, len(nums) - 1

            while l <= h:
                mid = l + (h - l) // 2

                if nums[mid] < nums[0] and nums[mid - 1] >= nums[0]:
                    return mid
                elif nums[mid] < nums[0]:
                    h = mid - 1
                else:
                    l = mid + 1

        minInd = findMin()
        arrLength = len(nums)

        def revertIndex(ind):
            return (ind + minInd) % arrLength

        l = 0
        h = len(nums) - 1

        while l <= h:
            mid = l + (h - l) // 2
            convertedMid = revertIndex(mid)

            if nums[convertedMid] == target:
                return convertedMid

            elif nums[convertedMid] < target:
                l = mid + 1

            else:
                h = mid - 1

        return -1
