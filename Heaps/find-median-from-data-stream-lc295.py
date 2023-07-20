# page 111
import heapq

# The idea is to maintain 2 heaps, one min heap and one max heap. Both these heaps will have half of the elements.
# The max heap will have the smaller half of the elements and the min heap will have the larger half of the elements.
# The median will be the average of the top elements of both the heaps if the number of elements is even.
# If the number of elements is odd, then the median will be the top element of the heap with more elements.

class MedianFinder:

    def __init__(self):
        self.smallMaxHeap, self.largeMinHeap = [], []

    def addNum(self, num: int) -> None:

        # if the num is greater than the top of the largeMinHeap, then it belongs to the larger half of the elements;
        # that is if the larger heap exists.
        if self.largeMinHeap and num > self.largeMinHeap[0]:
            heapq.heappush(self.largeMinHeap, num)

        else:
            heapq.heappush(self.smallMaxHeap, -1 * num) # -1 * num because it is a max heap

        # Balance the heaps
        # the '-1' multiplier to compensate for the negative values stored/ to be stored in the smallMaxHeap
        if len(self.smallMaxHeap) > len(self.largeMinHeap) + 1:
            heapq.heappush(self.largeMinHeap, -1 * heapq.heappop(self.smallMaxHeap))

        if len(self.largeMinHeap) > len(self.smallMaxHeap) + 1:
            heapq.heappush(self.smallMaxHeap, -1 * heapq.heappop(self.largeMinHeap))

    def findMedian(self) -> float:
        if len(self.smallMaxHeap) > len(self.largeMinHeap):
            return -1 * self.smallMaxHeap[0]

        elif len(self.smallMaxHeap) < len(self.largeMinHeap):
            return self.largeMinHeap[0]

        else:
            return (-1 * self.smallMaxHeap[0] + self.largeMinHeap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()