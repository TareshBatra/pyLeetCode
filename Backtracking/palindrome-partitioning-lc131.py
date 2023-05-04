# page 66
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.result = []

        def backtrack(start, part):

            if start == len(s):
                self.result.append(part.copy())

            for i in range(start, len(s)):
                if self.isPalindrome(s[start:i + 1]):
                    backtrack(i + 1, part + [s[start:i + 1]])

        backtrack(0, [])
        return self.result

    def isPalindrome(self, value):
        if len(value) == 0:
            return False

        if len(value) == 1:
            return True

        l, r = 0, len(value) - 1

        while l < r:
            if value[l] != value[r]:
                return False

            l += 1
            r -= 1

        return True
