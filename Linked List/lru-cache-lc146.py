# page 47

# using a double linked list
"""
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key2node = {}  # map key to node

        self.head, self.tail = Node(-1, -1), Node(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head # looping the linked list

    # remove node from list
    def remove(self, node):
        prev, after = node.prev, node.next
        prev.next, after.prev = after, prev

    # insert node at right
    def insert(self, node):
        prev, after = self.tail.prev, self.tail
        prev.next = after.prev = node
        node.next, node.prev = after, prev

    def get(self, key: int) -> int:
        if key in self.key2node:
            self.remove(self.key2node[key])
            self.insert(self.key2node[key])
            return self.key2node[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key2node:
            self.remove(self.key2node[key])
        self.key2node[key] = Node(key, value)
        self.insert(self.key2node[key])

        if len(self.key2node) > self.capacity:
            # remove from the list and delete the LRU from the dictionary
            lru = self.head.next
            self.remove(lru)
            del self.key2node[lru.key]

"""

from collections import OrderedDict


# using an ordered dictioanry

class LRUCache:

    def __init__(self, capacity: int):
        self.ordDict = OrderedDict()
        self.capacityLeft = capacity

    def get(self, key: int) -> int:
        if key not in self.ordDict:
            return -1

        else:
            val = self.ordDict.pop(key)

            # setting the key as the most recently used value
            self.ordDict[key] = val
            return val

    def put(self, key: int, value: int) -> None:
        if key in self.ordDict:
            self.ordDict.pop(key)

        else:
            if self.capacityLeft > 0:
                self.capacityLeft -= 1
            else:
                self.ordDict.popitem(last=False)

        self.ordDict[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
