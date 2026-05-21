class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        
        l, r = 0, n - 1
        maxLeft = height[0]
        maxRight = height[-1]
        water = 0

        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                water += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                water += maxRight - height[r]
        
        return water