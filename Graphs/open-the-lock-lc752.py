# page 95

from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadSet = set(deadends)

        if '0000' in deadSet:
            return -1

        q = deque()
        q.append(['0000', 0])
        visited = set()

        def getPerms(comb):
            permutations = []
            for i in range(len(comb)):
                fwdPerm = comb[:i] + str((int(comb[i]) + 1) % 10) + comb[i + 1:]
                revPerm = comb[:i] + str((int(comb[i]) - 1 + 10) % 10) + comb[i + 1:]

                permutations.extend([fwdPerm, revPerm])

            return permutations

        # bfs
        while q:
            comb, turns = q.popleft()

            if comb == target:
                return turns

            for perm in getPerms(comb):
                if perm not in visited and perm not in deadSet:
                    visited.add(perm)
                    q.append([perm, turns + 1])

        return -1
