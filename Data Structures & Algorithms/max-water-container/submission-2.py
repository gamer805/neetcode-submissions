class Solution:
    def maxArea(self, heights: List[int]) -> int:
        curr_area, max_area = 0, 0

        l, r = 0, len(heights) - 1

        while l < r:
            curr_area = min(heights[l], heights[r]) * (r - l)
            if curr_area > max_area:
                max_area = curr_area
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_area
        