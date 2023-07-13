from typing import List

# Greedy
# Time: O(n)
# Space: O(1)
class Solution:
    def jump(self, nums: List[int]) -> int:

        jumps = 0  # tracking the number of jumps
        ind = 0  # tracking the current index

        while ind < len(nums) - 1:

            maxJump, nextInd = 0, ind

            for i in range(1, nums[ind] + 1):  # checking all the possible jumps from the current index

                if ind + i >= len(nums) - 1:  # if we can reach the last index from the current index, we are done
                    nextInd = len(nums) - 1
                    break

                # the best jump that we can make from the current index is the one that takes us the farthest from
                # the next index, i.e., ind + i + nums[ind + i]
                # (ind + i) -> index after 1 jump from ind
                # (nums[ind + i]) -> number of jumps that we can make from (ind + i)
                # the sum of which ends up giving the farthest index we can reach from ind in 2 jumps

                elif ind + i + nums[ind + i] > maxJump:
                    maxJump = ind + i + nums[ind + i]
                    nextInd = ind + i

            ind = nextInd
            jumps += 1

        return jumps

# DP
# Time: O(n*max(nums))
# Space: O(n)

class Solution2:
    def jump(self, nums: List[int]) -> int:

        self.memo = {}

        def dp(i):
            if i >= len(nums) - 1:
                return 0

            if nums[i] == 0: # if we can't move forward from the current index, it's a dead end
                return float('inf')

            elif i in self.memo:
                return self.memo[i]

            else:
                res = 1 + min([dp(i + jump) for jump in range(1, nums[i] + 1)])
                self.memo[i] = res
                return self.memo[i]

        return dp(0)
