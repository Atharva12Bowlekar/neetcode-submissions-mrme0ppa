class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1
        max_vol = 0

        while l < r:
            vol = (r-l) * min(heights[l], heights[r])
            max_vol = max(vol, max_vol)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return max_vol
        