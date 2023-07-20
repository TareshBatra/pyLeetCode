# Up there with the hardest problems I've ever done. The solution is extremely intricate.
from typing import List


# The usage of a Trie is the key to this problem.
# In a nutshell the idea is that we create a trie of all the words given in the input list.
# Then we perform a DFS on the board from each cell, and at each cell we check if the current prefix is in the trie.
# This bit is already tricky enough to get right, but the real trick to avoid TLE is to remove the words as we find them
# from the trie. This optimization is necessary to avoid creating the same word multiple times.

class Trie:  # This is a trie node
    def __init__(self):
        self.children = {}  # dictionary of characters corresponding to the children of the current node
        self.currWordEnd = False  # boolean to indicate if the current node is the end of a word
        self.wordsLeft = 0  # (New) number of words left in the subtree of the current node. We must track this to allow
        # for the removal of words from the trie

    def insert(self, word: str) -> None:
        currNode = self  # to keep track of the current node (eqv. to self.root)
        currNode.wordsLeft += 1  # (New) increment the number of words left in the subtree of the current node

        for c in word:
            if c not in currNode.children:
                currNode.children[c] = Trie()

            currNode = currNode.children[c]
            currNode.wordsLeft += 1  # (New) increment the number of words left in the subtree of the new current node

        currNode.currWordEnd = True

    def removeWord(self, word: str) -> None:
        currNode = self
        currNode.wordsLeft -= 1  # (New) decrement the number of words left in the subtree of the current node

        for c in word:
            if c in currNode.children:
                currNode = currNode.children[c]
                currNode.wordsLeft -= 1  # (New) decrement the number of words left in the subtree of the new current node


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        # result is the set of words that can be created, could have been list too.
        # The reason behind choosing a set is to avoid duplicates. However, since we are removing words
        # from the trie as we find them, duplicates are not possible.
        result, visited = set(), set()

        self.root = Trie()  # root node of the trie

        for word in words:
            self.root.insert(word)  # creating the trie of words

        def dfs(r, c, node, word):
            # the node.wordsLeft > 0 condition is the key to the optimization, where if the number of words left in
            # the subtree of the current node is 0, we can stop the DFS from that node. This is because we are
            # removing words
            if r in range(m) and c in range(n) and (r, c) not in visited and len(node.children) > 0 and \
                    board[r][c] in node.children and node.wordsLeft > 0:
                visited.add((r, c))

                node = node.children[board[r][c]]
                word += board[r][c]

                if node.currWordEnd: # if we have found a word, we remove it from the trie and add it to the result

                    # since we are removing the word from the trie, we must set the currWordEnd for the node to False
                    # we can set this to false here or in the removeWord method of the Trie class, by adding
                    # currNode.currWordEnd = False in the removeWord method
                    node.currWordEnd = False

                    result.add(word) # add the word to the result
                    self.root.removeWord(word) # remove the word from the trie

                LRTB = [[-1, 0], [1, 0], [0, -1], [0, 1]] # left, right, top, bottom
                for dr in LRTB:
                    row, col = r + dr[0], c + dr[1]
                    dfs(row, col, node, word)

                visited.remove((r, c))

        for r in range(m):
            for c in range(n):
                dfs(r, c, self.root, "")

        return list(result)
