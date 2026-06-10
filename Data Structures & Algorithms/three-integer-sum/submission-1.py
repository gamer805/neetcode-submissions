class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        snums = nums

        for i in range(len(nums) - 2):
            if i > 0 and snums[i] == snums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = snums[i] + snums[l] + snums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    triplets.append([snums[i], snums[l], snums[r]])
                    while l < r and snums[l] == snums[l+1]:
                        l += 1
                    while l < r and snums[r] == snums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return triplets