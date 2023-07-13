from typing import List


# Greedy
# Time: O(n)
# Space: O(n)

class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        lastOccurence = {}  # to keep track of the last index of each character in the string

        for i in range(len(s)):
            lastOccurence[s[i]] = i

        result = []
        atLeastUntil = 0  # to keep track of the last index of the current partition
        startIndex = 0  # to keep track of the first index of the current partition

        while atLeastUntil < len(s):
            ind = startIndex

            # iterating over the current partition, while updating the last index of the partition
            # as per the lastIndices of the characters in the partition
            # We must at least iterate until the last index of the current character in the partition
            # to make sure that we don't miss any characters that are not present in the current partition

            while ind <= atLeastUntil:
                atLeastUntil = max(lastOccurence[s[ind]], atLeastUntil) # updating the last index of the partition
                ind += 1

            result.append(atLeastUntil - startIndex + 1) # appending the length of the current partition to the result
            atLeastUntil += 1
            startIndex = atLeastUntil # updating the start index of the next partition

        return result
