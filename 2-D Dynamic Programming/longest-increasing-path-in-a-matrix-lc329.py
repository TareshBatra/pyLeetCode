# page 84

from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        self.memo = {}

        def dfs(r, c, prev):
            if r < 0 or r >= m or c < 0 or c >= n or matrix[r][c] <= prev:
                return 0

            elif (r, c) in self.memo:
                return self.memo[(r, c)]

            else:
                res = 1
                res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
                res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
                res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
                res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))

                self.memo[(r, c)] = res
                return res

        answer = 0

        for r in range(m):
            for c in range(n):
                answer = max(answer, dfs(r, c, -1))

        return answer
