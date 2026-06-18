class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1
        if len(nums) == 1:
            return 0 if (nums[0] == target) else -1
        while l < r:
            cut = (r+l) // 2
            if nums[cut] > nums[r]:
                l = cut + 1
            else:
                r = cut
        
        start = l
        print(start)
        new_nums = nums[l:] + nums[:l]
        indices = list(range(l, len(nums))) + list(range(l))
        print(new_nums)

        l, r = 0, len(nums)
        while l < r:
            mid = (l+r) // 2
            if new_nums[mid] == target:
                return indices[mid]
            if new_nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        
        return -1
        