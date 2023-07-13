from typing import List


# Greedy
# Time: O(n)
# Space: O(1)

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        check = set()

        for trip in triplets:

            # Triplets with values exceeding the target can never be used in max operations
            if trip[0] > target[0] or trip[1] > target[1] or trip[2] > target[2]:
                continue

            # If we are able to find triplets with values at all indices <= target,
            # with at least one value equal to the target, for all 3 indices
            # we can use them in max operations to get the target triplet

            for ind in range(3):
                if trip[ind] == target[ind]:
                    check.add(ind)

        return len(check) == 3  # checking if we have a match at all 3 indices
