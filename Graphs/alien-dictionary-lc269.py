# page 106

from collections import defaultdict
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adjList = defaultdict(list)

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            minL = min(len(word1), len(word2))

            # if word1 is longer than word2 and word2 is a prefix of word1, then the order is invalid (weird edge case)
            if len(word1) > len(word2) and word1[:minL] == word2[:minL]:
                return ""

            # finding the first point of difference between word1 and word2, to establish the relative order
            # of the 2 differing characters
            for j in range(minL):
                if word1[j] != word2[j]:
                    adjList[word1[j]].append(word2[j])
                    break

        # if a char is present in visited => it has been visited. The Bool value indicates if it's in the current path
        visited = {}
        result = []  # to store the (reverse) topological ordering

        # topological sort / post order dfs

        # this function returns true if the current path has a cycle
        def dfs(char):
            if char in visited:
                # if the char has already been visited in the current path => there's a cycle
                return visited[char]

            visited[char] = True

            if char in adjList:
                for nei in adjList[char]:
                    if dfs(nei):
                        return True

            visited[char] = False
            result.append(char)

        for char in adjList:
            if dfs(char):  # if there's a cycle in the current path => invalid ordering
                return ""

        reversed(result)
        return "".join(result)
