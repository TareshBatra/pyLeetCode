# page 4

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsDict = {}

        for i, stri in enumerate(strs):
            sortedStri = ''.join(sorted(stri))
            if sortedStri in strsDict:
                strsDict[sortedStri].append(i)
            else:
                strsDict[sortedStri] = [i]

        result = []

        for sortedStri in strsDict:
            subAnswer = []

            for i in strsDict[sortedStri]:
                subAnswer.append(strs[i])

            result.append(subAnswer)

        return result
