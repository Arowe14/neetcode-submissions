class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        def recurse(index, subset):
            if index >= len(nums):
                res.append(subset)
                return
            
            
            recurse(index + 1, subset + [nums[index]])
            recurse(index + 1, subset)
            return
        
        for i in range(len(nums)):
            recurse(i + 1, [nums[i]])
        
        return res