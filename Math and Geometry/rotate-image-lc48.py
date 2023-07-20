from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # rotating the image by 90 degrees clockwise can be boiled down to 2 steps -
        # 1. reverse the order of rows
        # 2. take the transpose of the new matrix

        up, down = 0, len(matrix) - 1

        # reverse the rows or just do matrix.reverse()
        while up < down:
            matrix[up], matrix[down] = matrix[down], matrix[up]  # swapping rows
            up += 1
            down -= 1

        # transpose the matrix or just do matrix = [*zip(*matrix)]
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]  # swapping elements across the diagonal
