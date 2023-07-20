from typing import List


# Greedy Approach
# Time Complexity: O(nlogn)
# Space Complexity: O(n)

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        if not intervals:
            return 0

        meetingTimes = []
        maxRooms, currRooms = 0, 0

        # The idea is to store the start and end times of the meetings
        # and sort them by time. Then we can iterate through the list and
        # increment the currRooms count when we encounter a start time and
        # decrement the currRooms count when we encounter an end time.
        # By doing this, we can keep track of the maximum number of rooms

        # This is a very simple yet elegant idea

        for interval in intervals:
            meetingTimes.append((interval[0], 1))  # start time
            meetingTimes.append((interval[1], -1))  # end time

        meetingTimes.sort()  # sort by time

        for time in meetingTimes:
            currRooms += time[1]

            if time[1] > 0:
                maxRooms = max(maxRooms, currRooms)

        return maxRooms
