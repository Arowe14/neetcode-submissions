class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        for value in nums:
            if value in seen:
                return True
            seen.append(value)
        return False