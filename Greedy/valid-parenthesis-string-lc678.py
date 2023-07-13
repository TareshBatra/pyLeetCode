class Solution:
    def checkValidString(self, s: str) -> bool:

        # minOpen: minimum number of open parenthesis (i.e., '*' is considered as ')' - closing parenthesis)
        # maxOpen: maximum number of open parenthesis (i.e., '*' is considered as '(' - opening parenthesis)
        minOpen, maxOpen = 0, 0

        if len(s) == 1:  # if there is only one character in the string, it must be '*' to be valid
            return s[0] == '*'

        for c in s:

            if c == '(':
                minOpen += 1
                maxOpen += 1

            elif c == ')':
                minOpen -= 1
                maxOpen -= 1

            else:  # c == '*'
                minOpen -= 1
                maxOpen += 1

            # if at any point, maxOpen becomes negative, it means that there are more ')' than '(' and '*' combined
            if maxOpen < 0:
                return False

            #  if minOpen becomes negative, it means that there are more '*' and ')' than '('
            # to proceed further, we must balance the number of ')' and '(', to make sure that
            # this minOpen does not interfere with the balance of the subsequent string
            # It's like we are starting a new string from this point onwards, since the previous substring is balanced

            minOpen = max(0, minOpen)

        return minOpen == 0
