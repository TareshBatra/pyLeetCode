# page 74
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        nums1 = nums[1:]
        nums2 = nums[:-1]
        n = len(nums1)

        self.memo = {}

        def dp(idx, arr):
            if idx >= len(arr):
                return 0

            elif idx in self.memo:
                return self.memo[idx]

            else:
                self.memo[idx] = max(arr[idx] + dp(idx + 2, arr), dp(idx + 1, arr))
                return self.memo[idx]

        ans1 = dp(0, nums1)
        self.memo = {}
        ans2 = dp(0, nums2)

        return max(ans1, ans2)
