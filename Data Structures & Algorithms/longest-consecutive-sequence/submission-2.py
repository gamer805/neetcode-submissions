class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        sorted_nums = list(sorted(set(nums)))
        longest = 1
        streak = 1
        i = 0
        for i in range(len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i-1] + 1:
                streak += 1
            else:
                streak = 1
            if streak > longest:
                longest = streak
        
        return longest