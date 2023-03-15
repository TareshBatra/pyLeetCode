# page 23
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []

        def dfsParenthesis(opening, closing, s):
            if len(s) == n * 2:
                result.append(s)
                return

            if opening < n:
                dfsParenthesis(opening + 1, closing, s + '(')

            if closing < opening:
                dfsParenthesis(opening, closing + 1, s + ')')

        dfsParenthesis(0, 0, '')
        return result
