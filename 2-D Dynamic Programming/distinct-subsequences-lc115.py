# page 85
from functools import cache


class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        @cache  # either cache or self.memo
        # self.memo = {}

        def dp(i, j):
            if j >= len(t):
                return 1

            elif i >= len(s):
                return 0

            # elif (i,j) in self.memo:
            #     return self.memo[(i,j)]

            else:
                res = 0
                if s[i] == t[j]:
                    res += dp(i + 1, j + 1)  # trying to find t[j+1: ] in s[i+1 : ]

                res += dp(i + 1, j)  # trying another path using the next index of s, i.e., find t[j:] in s[i=1: ]
                # self.memo[(i,j)] = res

                return res

        return dp(0, 0)
