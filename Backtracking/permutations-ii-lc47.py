class Solution:
    def permuteUnique(self, nums):

        nums.sort()
        self.result = []

        def backtrack(usable, currPerm):
            if not usable:
                self.result.append(currPerm.copy())
                return

            i = 0

            while i < len(usable):
                currPerm.append(usable[i])
                backtrack(usable[:i] + usable[i + 1:], currPerm)
                currPerm.pop()
                i += 1

                while i < len(usable) and usable[i] == usable[i - 1]:
                    i += 1

        backtrack(nums, [])
        return self.result
    
    # alternate approach

    """
    def permuteUnique(self, nums):

        nums.sort()

        self.result = []
        self.currPerm = []

        visited = [False] * len(nums)

        def backtrack():
            if len(self.currPerm) == len(nums):
                self.result.append(self.currPerm.copy())
            else:
                for i in range(len(nums)):
                    if visited[i] or (i > 0 and nums[i-1] == nums[i] and not visited[i-1]):
                        continue
                    visited[i] = True
                    self.currPerm.append(nums[i])

                    backtrack()

                    self.currPerm.pop()
                    visited[i] = False

        backtrack()

        return self.result

    """

