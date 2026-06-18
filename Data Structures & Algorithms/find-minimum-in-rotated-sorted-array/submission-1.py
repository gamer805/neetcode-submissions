class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]
        while r > l:
            cut = (r+l) // 2
            if nums[cut] < nums[cut-1]:
                return nums[cut]
            if nums[l] < nums[cut]:
                l = cut
            elif nums[cut] < nums[r-1]:
                r = cut
        
        return nums[cut]
                
        