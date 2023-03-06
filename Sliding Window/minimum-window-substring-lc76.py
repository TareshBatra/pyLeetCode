# page 19

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        ctrT = Counter(t)

        required = len(ctrT)  # the number of unique characters that need to be matched
        l, r = 0, 0
        winStart, winEnd = -1, len(
            s)  # initialized in such a way that if there is an answer, these values wil always be updated

        while True:
            # move the right pointer while we haven't met the requirements
            if r < len(s) and required > 0:
                if s[r] in ctrT:
                    ctrT[s[r]] -= 1
                    if ctrT[s[r]] == 0:
                        required -= 1
                r += 1

            # move the left pointer until we do not have a surplus of characters in t
            elif l < len(s) and required == 0:
                # the update of minimal substring happens only when
                if r - l < winEnd - winStart:
                    winStart, winEnd = l, r
                    print(winStart, winEnd)

                if s[l] in ctrT:
                    if ctrT[s[l]] == 0:
                        required += 1
                    ctrT[s[l]] += 1
                l += 1

            else:
                break

        return s[winStart:winEnd] if winStart >= 0 else ""
