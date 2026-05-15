class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s % 2 != 0:
            return False
        
        s /= 2


        def recurse(x, i):
            if x > s or i >= len(nums):
                return False
            if x == s:
                return True
            
            return (recurse(x + nums[i], i + 1) or recurse(x, i + 1))
            
            
            
        
        return recurse(0, 0)
            

