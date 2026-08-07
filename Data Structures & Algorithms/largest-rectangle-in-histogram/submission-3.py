class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = [] # Storing height and index
        max_area = 0

        for i,h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, h))

        while stack:
            i, h = stack.pop()
            max_area = max(max_area, h * (len(heights) - i))
        
        return max_area



        