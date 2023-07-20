class Solution:
    def getSum(self, a: int, b: int) -> int:

        mask = 0xffffffff  # 32 bit mask in hexadecimal ( basically 1's 32 times in binary) to handle overflow

        while (b & mask) > 0:  # till there is a carry over
            carry = (a & b) << 1  # carry over is the AND of a and b, left shifted by 1 place
            a = (a ^ b)
            b = carry

        if b > 0:  # if we have a carry over at the MSB, => the sum is negative
            return (a & mask)  # mask to handle overflow

        else:
            return a
