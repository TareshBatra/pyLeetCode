# page3

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        self.hash = {}
        for num in nums:
            if num in self.hash:
                return True
                break
            else:
                self.hash[num] = 1
        return False
