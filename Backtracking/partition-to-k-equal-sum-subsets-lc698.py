# page 69
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        numsSum = sum(nums)

        if numsSum % k != 0:
            return False

        bucketSize = numsSum // k

        nums.sort(reverse=True)

        def backtrack(start, remaining, subSetSum, used):

            if remaining == 0:
                return True

            if subSetSum == bucketSize:
                return backtrack(0, remaining - 1, 0, used)

            if subSetSum > bucketSize:
                return False

            for i in range(start, len(nums)):

                # optimization to avoifd trying the already rejected elements of same value

                if i > 0 and used[i - 1] == False and (nums[i - 1] == nums[i]):
                    continue

                if not used[i]:

                    used[i] = True

                    if backtrack(i + 1, remaining, subSetSum + nums[i], used):
                        return True

                    used[i] = False

            return False

        return backtrack(0, k, 0, [False] * len(nums))
