class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)

        l = 0
        r = n - 1
        maximum = 0
        minimum = 0
        area = 1

        while l < r:
            minimum = min(heights[l], heights[r])
            area = minimum * (r - l)
            maximum = max(maximum, area)

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return maximum

        