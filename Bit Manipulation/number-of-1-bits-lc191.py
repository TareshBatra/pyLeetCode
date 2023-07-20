# O(<=32) solution; the loop runs only as many times as the number of 1s in the binary representation of n
class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            n = n & (n - 1)  # this operation removes the rightmost 1 in a binary number
            result += 1

        return result


# O(32) solution

class Solution2:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            result += n % 2  # only multiples of 2 have their LSB as 0
            n = n >> 1  # to shift the bits rightwards by 1 place

        return result
