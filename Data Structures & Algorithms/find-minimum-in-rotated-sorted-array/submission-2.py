class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]
        while l < r:
            cut = (r+l) // 2
            if nums[cut] > nums[r]:
                l = cut + 1
            else:
                r = cut
        
        return nums[l]
                
        