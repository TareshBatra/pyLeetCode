# page 112

from typing import List
import heapq, collections


# This a tricky question. The idea is to use a min heap to store the cards and their counts (min over the card values).
# Then we can pop the top element from the heap and use it as the starting point for the group.
# We can then pop the next groupSize - 1 elements from the heap and check if they are consecutive.
# They must be consecutive and have at least as many cards as the starting card.This is because to form groups
# with the smallest card, the only consecutive cards that can be used are the ones greater than it
# Cards whose frequency is greater than the starting card are pushed back into the heap with their frequency
# reduced by the starting card's frequency.

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        cardsDict = collections.Counter(hand)

        minHeap = []

        for card, count in cardsDict.items():
            heapq.heappush(minHeap, [card, count])

        while minHeap:
            prevCard, initialCount = heapq.heappop(minHeap)
            currGroup = [(prevCard, initialCount)]

            while len(currGroup) < groupSize:
                if not minHeap:
                    return False

                currCard, currCount = heapq.heappop(minHeap)

                if currCard != prevCard + 1 or currCount < initialCount:
                    return False

                currGroup.append((currCard, currCount))
                prevCard = currCard

            for card, count in currGroup:
                if count > initialCount:
                    heapq.heappush(minHeap, [card, count - initialCount])

        return True


# Using List (O(n**2))

"""
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        hand.sort()

        while hand:
            try:
                base = hand[0]
                for i in range(groupSize):
                    hand.remove(base+i)
            except:
                return False

        return True
"""
