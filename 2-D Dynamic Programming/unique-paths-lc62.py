# page 81
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.memo = {}

        def dp(i, j):
            if i == m - 1 and j == n - 1:
                return 1

            elif i >= m or j >= n:
                return 0

            elif (i, j) in self.memo:
                return self.memo[(i, j)]

            else:
                self.memo[(i, j)] = dp(i + 1, j) + dp(i, j + 1)
                return self.memo[(i, j)]

        return dp(0, 0)