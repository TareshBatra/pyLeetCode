from typing import List

# Greedy
# Time: O(n)
# Space: O(n)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        difference = []  # An array to find the difference between gas and cost per station
        negativeSum = 0

        for i in range(len(gas)):
            difference.append(gas[i] - cost[i])

            if gas[i] - cost[i] < 0:
                negativeSum += gas[i] - cost[i]

        if sum(difference) < 0:  # If the cost exceeds the gas, we can't complete the circuit
            return -1

        for i in range(len(gas)):  # to create the circular effect
            difference.append(difference[i])

        # Kadane's Algorithm
        # The index from which we can find the maximum subarray sum over the "difference" array is the answer

        currSum, maxSum, currIndex, maxIndex = 0, 0, 0, 0

        for i, diff in enumerate(difference):

            # if we have already a maxSum that is greater than the negativeSum, we can complete the circuit
            if maxSum + negativeSum >= 0:
                break

            if currIndex >= len(gas):  # once we circle back to starting from the first index, break
                break

            if diff < 0:
                if currSum + diff < 0:
                    currIndex = i + 1
                    currSum = 0

                else:
                    currSum = currSum + diff

            else:
                currSum += diff

                if currSum > maxSum:
                    maxIndex = currIndex
                    maxSum = currSum

        return maxIndex
