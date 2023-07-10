# page 94
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()

        m, n = len(board), len(board[0])

        def dfs(r, c):

            if r in range(m) and c in range(n) and board[r][c] == 'O' and (r, c) not in visited:

                visited.add((r, c))

                LRTB = [[-1, 0], [1, 0], [0, -1], [0, 1]]

                for dr in LRTB:
                    dfs(r + dr[0], c + dr[1])

            else:
                return

        # performing dfs from the Os at the boundaries to identify points part of their islands - unsurrounded

        for c in range(n):
            if board[0][c] == 'O':
                dfs(0, c)

            if board[m - 1][c] == 'O':
                dfs(m - 1, c)

        for r in range(m):
            if board[r][0] == 'O':
                dfs(r, 0)

            if board[r][n - 1] == 'O':
                dfs(r, n - 1)

        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O' and (r, c) not in visited:
                    board[r][c] = 'X'









