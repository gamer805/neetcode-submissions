class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        middle = int((r - l) / 2)
        while r - l > 1:
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                r = middle
            else:
                l = middle + 1
            middle = l+int((r - l) / 2)
            if middle >= len(nums):
                return -1
        
        if nums[middle] == target:
                return middle
        
        return -1
        