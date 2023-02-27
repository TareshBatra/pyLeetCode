# page 9

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while True:
            sum = numbers[start] + numbers[end]

            if sum == target:
                return [start + 1, end + 1]  # +1 due to the array being 1 indexed

            elif sum > target:
                end -= 1

            else:
                start += 1
