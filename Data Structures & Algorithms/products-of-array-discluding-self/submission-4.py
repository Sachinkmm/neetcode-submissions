class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zeros = 0
        product = 1
        for num in nums:
            if num == 0:
                zeros += 1
            else:
                product *= num
        
        if zeros > 1:
            return [0] * n
        
        res = [0] * n
        for i in range(n):
            if zeros > 0:
                if nums[i] == 0:
                    res[i] = product
            else:
                res[i] = product // nums[i]
        
        return res

            
        