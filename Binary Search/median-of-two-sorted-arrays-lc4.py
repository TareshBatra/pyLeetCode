# page 37

from typing import List


class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) < len(nums2):
            input1 = nums1
            input2 = nums2
        else:
            input1 = nums2
            input2 = nums1

        m = len(input1)
        n = len(input2)
        l = 0

        h = m  # since m > n the median must be between 0 and m
        medianPosition = (m + n + 1) // 2
        while l <= h:
            p1 = (l + h) // 2
            p2 = medianPosition - p1

            # the inf conditions are for when either ends of the array are reached by the pointer

            left_m = input1[p1 - 1] if p1 != 0 else float('-inf')
            right_m = input1[p1] if p1 != m else float('inf')

            left_n = input2[p2 - 1] if p2 != 0 else float('-inf')
            right_n = input2[p2] if p2 != n else float('inf')

            if left_m <= right_n and left_n <= right_m:
                if (m + n) % 2 == 0:
                    return (max(left_m, left_n) + min(right_m, right_n)) / 2
                else:
                    return max(left_m, left_n)
            elif left_m > right_n:
                h = p1 - 1
            else:
                l = p1 + 1
