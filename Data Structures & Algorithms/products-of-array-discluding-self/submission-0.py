class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        for i in range(1, len(nums)): # Products on left of index
            prefix[i] = nums[i - 1] * prefix[i - 1]
        
        for i in range(len(nums) - 2, -1, -1): # Products on right of index
            postfix[i] = nums[i + 1] * postfix[i + 1]
        
        res = []
        for i in range(len(nums)): # Multiply products
            res.append(prefix[i] * postfix[i])

        return res


