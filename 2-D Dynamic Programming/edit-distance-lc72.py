# page 86
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        self.memo = {}

        def dp(i, j):

            # when you have no more characters left in word2, delete all the remaining characters from word1
            if j >= len(word2):
                return len(word1) - i

            # when you have no characters left in word1, add all the remaining characters left in word2
            elif i >= len(word1):
                return len(word2) - j

            elif (i, j) in self.memo:
                return self.memo[(i, j)]

            else:
                if word1[i] == word2[j]:
                    self.memo[(i, j)] = dp(i + 1, j + 1)

                else:  # min of delete, replace, and insert
                    self.memo[(i, j)] = 1 + min(dp(i + 1, j), dp(i + 1, j + 1), dp(i, j + 1))

                return self.memo[(i, j)]

        return dp(0, 0)
