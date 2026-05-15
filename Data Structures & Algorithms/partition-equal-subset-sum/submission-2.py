class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        seen = {}

        if s % 2 != 0:
            return False
        
        s /= 2


        def recurse(x, i):
            if (x, i) in seen:
                return seen[(x, i)]

            if x > s or i >= len(nums):
                return False
            if x == s:
                return True
            
            result = (recurse(x + nums[i], i + 1) or recurse(x, i + 1))
            
            seen[(x, i)] = result
            return result
            
            
        
        return recurse(0, 0)
            

