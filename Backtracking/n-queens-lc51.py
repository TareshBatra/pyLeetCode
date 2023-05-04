# page 70

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.result = []

        def backtrack(r, cols, posDiag, negDiag, board):

            if r == n:
                boardStr = ["".join(row) for row in board]
                self.result.append(boardStr)
                return

            for c in range(n):

                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1, cols, posDiag, negDiag, board)

                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0, set(), set(), set(), [["."] * n for i in range(n)])

        return self.result
