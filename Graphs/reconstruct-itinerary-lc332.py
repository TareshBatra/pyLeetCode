# page 101

from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # to ensure that we check possible paths in lexical order
        tickets.sort()

        adjList = defaultdict(list)

        for src, dst in tickets:
            adjList[src].append(dst)

        result = ["JFK"]  # always starts at JFK

        def dfs(src):
            if len(result) == len(tickets) + 1:
                # i.e., we have exhausted our itinerary
                return True

            elif src not in adjList:
                # if no ticket exists starting from the source => wrong path
                return False

            # tricky bit: to allow backtracking
            else:
                tempList = adjList[src].copy()
                for ind, dst in enumerate(tempList):
                    # iterating over tempList since, we are modifying adjList[src] in the loop
                    adjList[src].pop(ind)
                    result.append(dst)

                    if dfs(dst):
                        return True

                    adjList[src].insert(ind, dst)  # to revert the "pop"
                    result.pop()  # to revert the "append"

                return False

        dfs("JFK")
        return result

