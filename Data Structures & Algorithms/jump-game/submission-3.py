class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Dynamic Programming
        # Go back from final node to ensure there's a way to reach that node
        # Once found, go back from that node to ensure there's a way to reach it 
        if len(nums) == 1:
            return True
        
        checkpoint = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= checkpoint:
                checkpoint = i
        
        return checkpoint == 0
            