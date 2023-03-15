# page 27
class SolutionRecursion:
    def decodeString(self, s: str) -> str:

        def recurseDecode(t):
            ind = 0
            strValue = ""
            while ind < len(t):
                if t[ind].isnumeric():
                    num = ""
                    nextIter = ""
                    while t[ind].isnumeric():  # to detetct multi-digit values
                        num += t[ind]
                        ind += 1
                    num = int(num)
                    ind += 1
                    openingBracs = 1

                    # finding the string enclosed within num as nextIter

                    while True:
                        if t[ind] == '[':
                            openingBracs += 1
                        elif t[ind] == ']':
                            openingBracs -= 1

                            if openingBracs == 0:
                                break

                        nextIter += t[ind]
                        ind += 1

                    strValue += recurseDecode(nextIter) * num
                    ind += 1

                elif t[ind].isalpha:
                    strValue += t[ind]
                    ind += 1

            return strValue

        if s.isnumeric():
            return ""
        else:
            return recurseDecode(s)


class SolutionStack:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char == ']':
                presentString = ""
                presentNumber = 0

                while stack[-1] != '[':
                    presentString = stack.pop() + presentString

                stack.pop()
                multiplier = 1
                while stack and stack[-1].isnumeric():
                    presentNumber = presentNumber + multiplier * int(stack.pop())
                    multiplier *= 10

                print(presentNumber)

                presentString = presentString * presentNumber

                stack.append(presentString)

            else:
                stack.append(char)

        if s.isnumeric():
            return ""
        else:
            return "".join(stack)
