class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = 0
        x = 0

        for i, n in enumerate(nums):
            s += i
            x += n
        
        return (s + len(nums) - x)