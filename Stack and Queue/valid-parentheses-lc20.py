# page 22
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracDict = {'(': ')', '{': '}', '[': ']'}

        for brac in s:
            if brac in bracDict.keys():
                stack.append(brac)

            elif stack and brac == bracDict[stack[-1]]:
                # important to verify the stack is not empty before making the comparison
                stack.pop()

            else:
                return False

        return len(stack) == 0
