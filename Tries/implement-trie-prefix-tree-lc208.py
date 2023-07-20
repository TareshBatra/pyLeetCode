class Node:  # Trie Node
    def __init__(self):
        self.children = {}  # dictionary of characters corresponding to the children of the current node
        self.currWordEnd = False  # boolean to indicate if the current node is the end of a word


class Trie:

    def __init__(self):
        self.root = Node()  # root node of the trie

    def insert(self, word: str) -> None:  # inserting a word into the trie
        currNode = self.root  # to keep track of the current node

        for c in word:  # iterating through the characters of the word
            if c not in currNode.children:  # if the character is not in the children of the current node, add it
                currNode.children[c] = Node()
            # update the current node to the node corresponding to the current character
            currNode = currNode.children[c]

            # The last node of the word (corresponding to the last character) is marked as the end of the word
        currNode.currWordEnd = True

    def search(self, word: str) -> bool:
        currNode = self.root

        for c in word:
            if c not in currNode.children:  # if the character is not in the children of the current node, return False
                return False

            currNode = currNode.children[c]

        return currNode.currWordEnd  # to make sure that the word is actually present in the trie and not just a prefix

    def startsWith(self, prefix: str) -> bool:
        currNode = self.root

        for c in prefix:
            if c not in currNode.children:
                return False

            currNode = currNode.children[c]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
