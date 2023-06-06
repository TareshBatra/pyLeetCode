# page 74
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLength = 0
        maxSubs = ""

        for i in range(len(s)):

            # odd length palindromes centered at s[i]
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLength:
                    maxSubs = s[l:r + 1]
                    maxLength = r - l + 1
                l -= 1
                r += 1

            # even length palindromes centered at s[i] and s[i+1]
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLength:
                    maxSubs = s[l:r + 1]
                    maxLength = r - l + 1
                l -= 1
                r += 1

        return maxSubs
