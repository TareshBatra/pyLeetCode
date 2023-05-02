# page 66

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        alreadyUsed = set()

        def backtrack(r, c, i):
            if i == len(word):
                return True

            if r < 0 or r >= m or c < 0 or c >= n or word[i] != board[r][c] or (r, c) in alreadyUsed:
                return False

            alreadyUsed.add((r, c))
            result = backtrack(r - 1, c, i + 1) or backtrack(r + 1, c, i + 1) or backtrack(r, c - 1,
                                                                                           i + 1) or backtrack(r, c + 1,
                                                                                                               i + 1)
            alreadyUsed.remove((r, c))
            return result

        # To prevent time limit exceeded,reverse the word if frequency of the first letter is more than the last
        # letter's

        # defaultdict never raises a key error...

        # count = defaultdict(int, sum(map(Counter, board), Counter()))
        # if count[word[0]] > count[word[-1]]:
        #     word = word[::-1]

        for r in range(m):
            for c in range(n):
                if backtrack(r, c, 0):
                    return True
        return False
