class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = set(nums)
        seq = 0

        for num in nums:
            # Check if start of sequence
            if num - 1 not in d:
                length = 0
                while (num + length) in d:
                    length += 1
                seq = max(seq, length)

        
        return seq