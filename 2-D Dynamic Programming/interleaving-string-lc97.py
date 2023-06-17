# page 83

'''
The idea here is to continue checking whether the first character in the remnant subtring of s3 appears
in the remnant substrings of s1 and s2. Subsequently, continue recursing until we reach the end of s1 or s2.
'''


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.memo = {}

        def intLeave(i, j):

            if (i, j) in self.memo.keys():
                return self.memo[(i, j)]

            elif (i >= len(s1)):
                if s2[j:] == s3[i + j:]:
                    self.memo[(i, j)] = True
                    return self.memo[(i, j)]
                else:
                    self.memo[(i, j)] = False
                    return self.memo[(i, j)]

            elif (j >= len(s2)):
                if s1[i:] == s3[i + j:]:
                    self.memo[(i, j)] = True
                    return self.memo[(i, j)]
                else:
                    self.memo[(i, j)] = False
                    return self.memo[(i, j)]

            else:

                if (s1[i] == s3[i + j] and s2[j] != s3[i + j]):
                    self.memo[(i, j)] = intLeave(i + 1, j)
                    return self.memo[(i, j)]
                elif (s2[j] == s3[i + j] and s1[i] != s3[i + j]):
                    self.memo[(i, j)] = intLeave(i, j + 1)
                    return self.memo[(i, j)]
                elif (s1[i] == s3[i + j] and s2[j] == s3[i + j]):
                    self.memo[(i, j)] = intLeave(i + 1, j) or intLeave(i, j + 1)
                    return self.memo[(i, j)]
                else:
                    self.memo[(i, j)] = False
                    return self.memo[(i, j)]

        if len(s1) + len(s2) == len(s3):
            return intLeave(0, 0)
        else:
            return False

