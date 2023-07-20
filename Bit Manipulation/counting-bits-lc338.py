# O(n) solution
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:

        result = [0]
        # the offset is the power of 2 being used in the current MSB.
        # It is updated everytime we encounter a power of 2, i.e., when we have a new MSB

        offset = 1  # initially it's 1, because 2^0 = 1

        for i in range(1, n + 1):
            if i == offset * 2:  # if we encounter a power of 2, we update the offset
                offset = i

                # the number of set bits in the current number is
            # 1 + the number of set bits in the number obtained by removing the MSB
            # e.g., 6 = 110, 6 - 4 = 2 = 10, 2 has 1 set bit
            # so, 6 has 1 + 1 = 2 set bits
            # e.g., 7 = 111, 7 - 4 = 3 = 11, 3 has 2 set bits
            # so, 7 has 1 + 2 = 3 set bits, etc.
            # the idea is to use the previously calculated results to calculate the current result, like dp

            result.append(1 + result[i - offset])

        return result
