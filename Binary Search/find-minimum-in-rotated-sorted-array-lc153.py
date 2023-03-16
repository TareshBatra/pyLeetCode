# page 33

class Solution:
    def findMin(self, nums: list[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]

        l, h = 0, len(nums) - 1

        while l <= h:
            mid = l + (h - l) // 2
            # the value at nums[mid-1] for nums[mid] being the least value will be the max value
            # if mid-1 is 0, that's why we provide the condition of >=
            if nums[mid] < nums[0] and nums[mid - 1] >= nums[0]:
                return nums[mid]
            elif nums[mid] < nums[0]:
                h = mid - 1
            else:
                l = mid + 1
