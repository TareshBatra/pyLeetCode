# page 110

from typing import List
import collections
import heapq


# The idea is to execute the tasks with the highest frequency as frequently as possible.
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        tasksDict = collections.Counter(tasks)  # getting the frequency of each task
        maxHeap = []
        time = 0

        # pushing the negative frequency values for each task to make it a max heap
        for task, t in tasksDict.items():
            heapq.heappush(maxHeap, [-t, task])

        # maintaining a queue for the tasks that have just been executed to be pushed back to the heap
        # in a FIFO manner after the cooldown period
        task_q = collections.deque()

        while maxHeap:
            i = 0

            # i is used to keep track of the number of tasks executed in the current cycle to track the cooldown period
            while i <= n:
                time += 1

                if maxHeap:
                    cnt, task = heapq.heappop(maxHeap)

                    if cnt < -1:  # if the count == -1 => the task has already been executed to the required frequency
                        task_q.append([cnt + 1, task])

                if not maxHeap and not task_q:  # all tasks have been executed to the required frequency
                    break

                # if there are still tasks in task_q waiting to be executed, but the cooldown period is not over yet
                else:
                    i += 1

            # pushing the tasks in the queue back to the heap after the cooldown period in a FIFO manner
            while task_q:
                heapq.heappush(maxHeap, task_q.popleft())

        return time
