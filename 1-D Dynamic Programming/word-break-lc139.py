# page 77
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        self.memo = {}

        def backtrack(start):

            if start >= len(s):
                return True

            if start in self.memo:
                return self.memo[start]

            currSubstr = ""
            result = False

            for i in range(start, len(s)):
                currSubstr += s[i]

                if currSubstr in wordDict:
                    result = backtrack(i + 1)

                    if result:
                        break

            self.memo[start] = result
            return self.memo[start]

        return backtrack(0)

# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:

#         dp = [False] * (len(s) + 1)
#         dp[len(s)] = True

#         for i in range(len(s) - 1, -1, -1):
#             for w in wordDict:
#                 if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
#                     dp[i] = dp[i + len(w)]
#                 if dp[i]:
#                     break

#         return dp[0]
