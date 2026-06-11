class Solution:
    def trap(self, height: List[int]) -> int:

        max_area = 0
        l, r = 0, len(height) - 1
        left_max, right_max = 0, 0
        counted = []
        while l < r:
            if height[l] < height[r]:
                if height[l] >= left_max:
                    left_max = height[l]
                else:
                    max_area += left_max - height[l]
                l += 1
            else:
                if height[r] >= right_max:
                    right_max = height[r]
                else:
                    max_area += right_max - height[r]
                r -= 1
        
        return max_area

        