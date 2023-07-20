from typing import List


# Time: O(m*n)
# Space: O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # The main idea is to use the first row and first column as the markers to check if a row or column has any zero
        # If any element is zero, set the first element of that row and column to zero
        # Re-iterate over the matrix [1:][1:] & set the cells to zero if the first cell of that row or column is zero
        # Finally, check if the first row has any zero, if so, set the entire row to zero
        # Also, Check if the first column has any zero, if so, set the entire column to zero

        m, n = len(matrix), len(matrix[0])
        rowZero = False  # to check if the first row has any zero

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:  # if any element is zero
                    matrix[0][c] = 0  # set the first element of that column to zero

                    if r > 0:  # if the row is not the first row
                        matrix[r][0] = 0  # set the first element of that row to zero
                    else:
                        rowZero = True  # if the row is the first row, set rowZero to True

        for r in range(1, m):  # start from 1 because we don't want to change the first row
            for c in range(1, n):  # start from 1 because we don't want to change the first column
                if matrix[r][0] == 0 or matrix[0][c] == 0:  # if any of the first elements of the row or column is zero
                    matrix[r][c] = 0  # set the element to zero

        if matrix[0][0] == 0:  # if the first element of the matrix is zero
            for r in range(m):  # set all the elements of the first column to zero
                matrix[r][0] = 0

        if rowZero:  # if the first row had any zero
            for c in range(n):  # set all the elements of the first row to zero
                matrix[0][c] = 0


# Time: O(m*n)
# Space: O(m+n)
class Solution2:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m, n = len(matrix), len(matrix[0])
        row = set()
        column = set()

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    row.add(r)
                    column.add(c)

        for r in range(m):
            for c in range(n):
                if r in row or c in column:
                    matrix[r][c] = 0
