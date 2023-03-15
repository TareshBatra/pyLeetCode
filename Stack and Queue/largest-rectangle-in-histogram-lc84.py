# page 30

class Solution:
    def largestRectangleArea(self, heights):
        heights.append(0) # to make sure that the last entry is the least and all values are popped
        stack = []
        maxArea = 0

        for i in range(len(heights)):

            while stack and heights[i] < heights[stack[-1]]:

                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height * width)

            stack.append(i)

        return maxArea