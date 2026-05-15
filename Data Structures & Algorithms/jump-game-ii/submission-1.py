class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        moves = 1 
        maxx = 0
        x = nums[0]
        for i in range(len(nums) - 1):
            maxx = max(maxx, nums[i])            
            if x == 0:
                x = maxx
                moves += 1
            maxx -= 1
            x -= 1

        return moves