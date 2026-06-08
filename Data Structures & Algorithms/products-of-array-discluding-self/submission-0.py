class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product_nz = 1
        zero_locs = []
        for i in range(len(nums)):
            if nums[i] != 0:
                product_nz *= nums[i]
            else:
                zero_locs.append(i)

        
        result = []
        one_zero = len(zero_locs) == 1
        many_zeros = len(zero_locs) > 1
        for i in range(len(nums)):
            if many_zeros:
                result.append(0)
            elif nums[i] == 0:
                result.append(product_nz)
            elif one_zero:
                result.append(0)
            else:
                result.append(int(product_nz/nums[i]))
        
        return result