class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        res = nums[0]
        cur = 0

        for n in nums:
            if cur + n < n:
                cur = n
            else:
                cur += n
            
            res = max(res, cur)

        return res
        

            
            
            
            
            
