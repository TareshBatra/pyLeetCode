# page 7

import collections
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        """
        using defaultdict over a normal dictionary to remove keyErrors, so we do not have to worry about initializing the keys.

        """

        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        blocks = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                elif (
                        board[r][c] in rows[r]
                        or board[r][c] in cols[c]
                        or board[r][c] in blocks[(r // 3, c // 3)]  # using // to get the integer quotient
                ):
                    return False

                else:
                    cols[c].add(board[r][c])
                    rows[r].add(board[r][c])
                    blocks[(r // 3, c // 3)].add(board[r][c])

        return True
