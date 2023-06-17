# page 88
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # @cache
        self.memo = {}

        def dp(i, j):
            if j == len(p):  # If j has reached the end of p
                return i == len(s)  # check if i has reached the end of s

            elif (i, j) in self.memo:
                return self.memo[(i, j)]

            elif j < len(p) - 1 and p[j + 1] == '*':
                ans = dp(i, j + 2)  # match zero chars

                if i < len(s) and (s[i] == p[j] or p[j] == '.'):
                    # match 1 char, skip 1 char in s, don't skip in p since it can match one or more characters
                    ans = ans or dp(i + 1, j)
                self.memo[(i, j)] = ans
                return self.memo[(i, j)]

            elif i < len(s) and (p[j] == '.' or s[i] == p[j]):
                self.memo[(i, j)] = dp(i + 1, j + 1)  # match 1 char, skip 1 char in both s and p
                return self.memo[(i, j)]

            else:
                return False

        return dp(0, 0)
