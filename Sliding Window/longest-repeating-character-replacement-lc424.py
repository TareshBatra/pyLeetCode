# page 16

# naive solution
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        winStart = 0
        charDict = {}
        result = 0

        for winEnd in range(len(s)):
            char = s[winEnd]
            charDict[char] = 1 + charDict.get(char, 0) # pythonic way of saying, if char exists, fetch it and add 1 to the count, else, initialize it to 0 and add 1.
            maxElementFrequency = max(charDict.values()) # Fetching the maximum frequency from the dictionary each time it's updated.

            if (winEnd - winStart + 1) - maxElementFrequency > k : # length of the substring - maxFreq > k
                charDict[s[winStart]] -= 1
                winStart += 1

            else:
                result = max(result, winEnd - winStart + 1)

        return result

"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        winStart = 0
        maxFrequency = 0
        charDict = {}
        result = 0

        for winEnd in range(len(s)):
            char = s[winEnd]
            charDict[char] = 1 + charDict.get(char, 0)  # pythonic way of saying, if char exists, fetch it and add 1 to the count, else, initialize it to 0 and add 1.
            maxFrequency = max(maxFrequency, charDict[char])

            if (winEnd - winStart + 1) - maxFrequency > k:  # length of the substring - maxFreq > k
                charDict[s[winStart]] -= 1
                winStart += 1

            else:
                result = max(result, winEnd - winStart + 1)

        return result
