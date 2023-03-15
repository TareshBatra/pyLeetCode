# page 29

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while stack and k and stack[-1] > n:
                stack.pop()
                k -= 1

            # if the stack already has some values, no problem but if it does not, the first value should not be 0
            if stack or n is not '0':
                stack.append(n)

        # if not fully used
        if k: stack = stack[0:-k]

        return ''.join(stack) or '0'
