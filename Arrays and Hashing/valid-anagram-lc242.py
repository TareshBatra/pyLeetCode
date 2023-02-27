# page 3

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stringDict = {}

        # Creating a dictionary for s
        for char in s:
            if char in stringDict:
                stringDict[char] += 1
            else:
                stringDict[char] = 1

        for char in t:
            if char in stringDict:
                if stringDict[char] == 1:
                    # to delete entries which have already been used in t
                    del stringDict[char]
                else:
                    stringDict[char] -= 1

            else:
                return False

        if len(stringDict) == 0:
            return True
