class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []   # index, value

        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][1]:
                stackI, stackH = stack.pop()
                area = stackH * (i-stackI)
                max_area = max(area, max_area)
                start = stackI
            stack.append([start, height])

        print(stack)

        for i, height in stack:
            area = height * (len(heights)-i) 
            max_area = max(area, max_area)

        return max_area
        
        