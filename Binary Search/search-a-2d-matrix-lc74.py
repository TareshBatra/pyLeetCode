# page 33

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        def create2DRep(num):
            return [num // m, num % m]

        l, h = 0, m * n - 1

        while l <= h:
            mid = l + (h - l) // 2
            mid2d = create2DRep(mid)

            if target == matrix[mid2d[0]][mid2d[1]]:
                return True

            elif target > matrix[mid2d[0]][mid2d[1]]:
                l = mid + 1

            else:
                h = mid - 1

        return False
