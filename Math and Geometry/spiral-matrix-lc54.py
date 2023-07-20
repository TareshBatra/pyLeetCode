from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        m, n = len(matrix), len(matrix[0])

        # the idea is to keep popping the top most row
        # and then transform the matrix into the upside down version of its transpose (rotate 90 degrees anti-clockwise)
        # and repeat the process until the matrix is empty

        # eg. [[1,2,3],[4,5,6],[7,8,9]]
        # pop [1,2,3] and add it to the result list
        # transform [[4,5,6],[7,8,9]] into [[6,9],[5,8],[4,7]]
        # add [6,9] to the result list
        # transform [[5,8],[4,7]] into [[8,7],[5,4]]
        # add [8,7] to the result list
        # transform [[5,4]] into [[4],[5]]
        # add [4] to the result list
        # transform [[5]] into [[5]]
        # add [5] to the result list

        while matrix:

            # pop the top most row -
            result.extend(matrix.pop(0))

            # upside down version of the matrix transpose
            matrix = [*zip(*matrix)]
            matrix.reverse()

        return result

