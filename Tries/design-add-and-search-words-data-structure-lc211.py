class Node:  # Trie Node
    def __init__(self):
        self.children = {}
        self.currWordEnd = False


class WordDictionary:

    def __init__(self):  # initializing the trie
        self.root = Node()

    def dfs(self, node, target):  # dfs to search for the target word

        # if the target word is empty, we are at the end of the word. So, if the current node is marked as
        # the end of a word, return True
        if target == '':
            return node.currWordEnd

        # if all that's left of the target word is '.', we just need to check if any of the children of the current node
        # are marked as the end of a word. If so, return True; else return False
        elif target == '.':
            for c in node.children.keys():
                if node.children[c].currWordEnd:
                    return True

            return False

        # if the first character of the target word is '.', we need to check if any of the children of the current node
        # can lead to a word that matches the rest of the target word. If so, return True; else return False.
        # Thus, we recursively call dfs on all the children of the current node.
        elif target[0] == '.':
            for c in node.children.keys():
                if self.dfs(node.children[c], target[1:]):
                    return True

        # This is the normal case. If the first character of the target word is not '.', we need to check if the current
        # node has a child corresponding to the first character of the target word. If so, we recursively call dfs
        # on the child of the current node corresponding to the first character of the target word and the rest
        # of the target word.
        elif target[0] in node.children:
            return self.dfs(node.children[target[0]], target[1:])

        # If none of the above conditions are satisfied, return False
        return False

    def addWord(self, word: str) -> None:  # inserting a word into the trie
        currNode = self.root

        for c in word:
            if c not in currNode.children:
                currNode.children[c] = Node()

            currNode = currNode.children[c]

        currNode.currWordEnd = True

    def search(self, word: str) -> bool:
        currNode = self.root
        return self.dfs(currNode, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
