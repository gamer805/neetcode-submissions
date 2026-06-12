class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        max_vals = []
        for i in range(len(nums)-k+1):
            curr_max = nums[i]
            j = 0
            while j < k and i + j < len(nums):
                curr_max = max(curr_max, nums[i+j])
                j += 1
            max_vals.append(curr_max)
        
        return max_vals
        