class Solution:
    def search(self, nums: List[int], target: int) -> int:
        remainder = list(enumerate(nums))
        while len(remainder) > 1:
            middle = int(len(remainder) / 2)
            if remainder[middle][1] == target:
                return remainder[middle][0]
            elif remainder[middle][1] > target:
                remainder = remainder[:middle]
            else:
                remainder = remainder[middle+1:]
        
        if remainder and remainder[0][1] == target:
            return remainder[0][0]
        
        return -1
        