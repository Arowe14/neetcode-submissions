class Solution:
    def trap(self, height: List[int]) -> int:
        pre = [0] * len(height)
        suf = [0] * len(height)

        pre[0] = height[0]
        for i in range(1, len(height)):
            pre[i] = max(height[i], pre[i - 1])

        suf[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            suf[i] = max(height[i], suf[i + 1])
        
        water = 0
        for i, h in enumerate(height):
            water += min(pre[i], suf[i]) - h
        
        return water