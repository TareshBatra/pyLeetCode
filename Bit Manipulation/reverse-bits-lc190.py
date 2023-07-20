class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for i in range(32):
            bit = (n >> i) & 1  # fetching the ith bit while right shifting n for subsequent iterations
            result = result | (bit << (31 - i))  # updating the (31-i)th bit of result

        return result
