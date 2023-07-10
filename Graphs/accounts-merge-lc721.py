# page 99
from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email2Account = {}

        parent, rank = [], []

        for i in range(len(accounts)):
            parent.append(i)
            rank.append(1)

        def find(node):
            p = parent[node]
            while p != parent[p]:
                p = parent[p]

            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            elif rank[p1] >= rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]

            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return True

        for ind, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in email2Account:
                    union(ind, email2Account[email])
                else:
                    email2Account[email] = ind

        emailGroup = defaultdict(list)  # index of acc -> list of emails

        for e, i in email2Account.items():
            leader = find(i)
            emailGroup[leader].append(e)

        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))  # array concat
        return res
