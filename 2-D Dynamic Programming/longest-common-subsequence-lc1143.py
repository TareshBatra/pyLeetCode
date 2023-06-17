# page 81
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.memo = {}

        def dp(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0

            elif (i, j) in self.memo:
                return self.memo[(i, j)]

            else:

                if text1[i] == text2[j]:
                    self.memo[(i, j)] = 1 + dp(i + 1, j + 1)

                else:
                    self.memo[(i, j)] = max(dp(i + 1, j), dp(i, j + 1))

                return self.memo[(i, j)]

        return dp(0, 0)
