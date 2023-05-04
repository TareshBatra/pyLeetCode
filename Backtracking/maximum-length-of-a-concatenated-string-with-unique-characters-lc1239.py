# page 69
from typing import List
from collections import Counter


class Solution:
    def maxLength(self, arr: List[str]) -> int:

        self.maxL = 0

        def backtrack(start, charSet):

            self.maxL = max(len(charSet), self.maxL)

            for i in range(start, len(arr)):
                if not self.commonAlph(charSet, arr[i]):
                    # *charSet,*add is to parse the union of the charSet and add
                    backtrack(i + 1, {*charSet, *set(arr[i])})

        backtrack(0, set())
        return self.maxL

    def commonAlph(self, str1, str2):
        ctr = Counter(str1) + Counter(str2)
        return max(ctr.values()) > 1

# Alternate Approach

# class Solution:
#     def maxLength(self, arr: List[str]) -> int:

#         def backtrack(start, charSet):

#             if start == len(arr):
#                 return len(charSet)

#             result = 0

#             if not self.commonAlph(charSet,arr[start]):
#                 result = backtrack(start+1, {*charSet,*set(arr[start])})

#             return max(backtrack(start+1, charSet), result)

#         return backtrack(0, set())


#     def commonAlph(self, str1, str2):
#         ctr = Counter(str1) + Counter(str2)
#         return max(ctr.values())> 1
