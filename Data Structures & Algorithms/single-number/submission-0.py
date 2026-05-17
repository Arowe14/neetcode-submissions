class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for num in nums: # Bitwise XOR
            res = num ^ res
        return res