# page 18

# naive sliding window

"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Dict = {}

        for char in s1:
            s1Dict[char] = 1 + s1Dict.get(char,0)

        winStart = 0
        s2SubDict = {}


        for winEnd in range(len(s2)):

            s2SubDict[s2[winEnd]] = 1 + s2SubDict.get(s2[winEnd],0)

            if winEnd - winStart + 1 == len(s1):

                if s2SubDict == s1Dict:
                    return True

                else:
                    s2SubDict[s2[winStart]] -= 1

                    if s2SubDict[s2[winStart]] == 0: del s2SubDict[s2[winStart]] # important to delete keys with
                    # value = 0, tp ensure that comparison of the dictionaries is not affected.

                    winStart += 1

        return False

"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1Dict = {}

        for char in s1:
            s1Dict[char] = 1 + s1Dict.get(char, 0)

        difference = len(s1Dict)
        s2SubDict = {}

        winStart = 0

        for winEnd in range(len(s2)):

            if s2[winEnd] in s1Dict:

                s2SubDict[s2[winEnd]] = 1 + s2SubDict.get(s2[winEnd], 0)

                if s2SubDict[s2[winEnd]] == s1Dict[s2[winEnd]]:
                    difference -= 1

                    if difference == 0:
                        return True

                elif s2SubDict[s2[winEnd]] > s1Dict[s2[winEnd]]:
                    # pruning the substring from the LHS (winStart pointer) until the character in excess is found
                    while s2[winEnd] != s2[winStart]:
                        # if the balance of characters found while pruning is disturbed, the difference must be changed
                        if s2SubDict[s2[winStart]] == s1Dict[s2[winStart]]:
                            difference += 1

                        s2SubDict[s2[winStart]] -= 1
                        winStart += 1

            else:
                # if a character is not in s1, then we must start over
                winStart = winEnd + 1
                s2SubDict = {}
                difference = len(s1Dict)

        return False
