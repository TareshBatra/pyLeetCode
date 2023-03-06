# page 15

# with winEnd and winStart. Essentially, the same solution but with a more defined sense of the sliding window

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        subStrWindow = set()
        winStart = 0
        for winEnd in range(len(s)):

            if s[winEnd] in subStrWindow:
                while s[winEnd] in subStrWindow:
                    subStrWindow.remove(s[winStart])
                    winStart += 1
                subStrWindow.add(s[winEnd])

            else:
                subStrWindow.add(s[winEnd])

            result = max(result, len(subStrWindow))

        return result
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        subStrWindow = set()
        winStart = 0
        for char in s:
            while char in subStrWindow:
                subStrWindow.remove(s[winStart])
                winStart += 1

            subStrWindow.add(char)
            result = max(result, len(subStrWindow))

        return result
