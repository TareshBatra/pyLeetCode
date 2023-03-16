# page 36

from typing import List


# binary search over the possible sums and return the minimum possible sum with k sub-arrays
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, h = max(nums), sum(nums)
        minSum = h

        def possible(sumVal):
            onGoingSum = 0
            partitions = k
            for num in nums:
                if onGoingSum + num > sumVal:

                    onGoingSum = 0
                    partitions -= 1

                    if partitions == 0:
                        return False

                onGoingSum += num

            return True

        while l <= h:
            mid = l + (h - l) // 2

            if possible(mid):
                minSum = min(minSum, mid)
                h = mid - 1

            else:
                l = mid + 1

        return minSum
