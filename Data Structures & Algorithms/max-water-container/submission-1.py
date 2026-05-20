class Solution:
    def maxArea(self, heights: List[int]) -> int:
        a = 0

        l, r = 0, len(heights) - 1

        while l < r:
            h = min(heights[l], heights[r])
            area = h * (r - l)

            a = max(a, area)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
            
        return a