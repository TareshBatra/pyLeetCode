# page 29

# O(nk)
"""
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for char in s:
            if len(stack) >= k-1:
                found = True
                for j in range(k-1):
                    if stack[-(j+1)] != char:
                        found = False
                        break

                if found:
                    for j in range(k-1):
                        stack.pop()
                else:
                    stack.append(char)

            else:
                stack.append(char)

        return "".join(stack)
"""


# O(n)
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # [char, count]

        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1

                if stack[-1][1] == k:
                    stack.pop()

            else:
                stack.append([char, 1])

        result = ""
        for char, count in stack:
            result += char * count

        return result
