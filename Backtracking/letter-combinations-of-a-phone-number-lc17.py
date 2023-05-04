# page 68
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        dig2Alph = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        self.result = []

        def backtrack(digitIdx, currStr):
            if digitIdx == len(digits):
                self.result.append(currStr)

            else:
                for char in dig2Alph[digits[digitIdx]]:
                    backtrack(digitIdx + 1, currStr + char)

        backtrack(0, '')
        return self.result
