# page 22

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []

        for token in tokens:
            if token in operators:
                operand2, operand1 = stack.pop(), stack.pop()
                result_str = operand1 + token + operand2
                stack.append(str(int(eval(result_str))))

            else:
                stack.append(token)

        return int(stack[0])
