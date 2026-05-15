class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        if k < 0:
            return []
        right = k - 1



        def find_max(left: int, right: int, nums: List[int], prev_max: int|None) -> int:
            if not prev_max:
                return max(nums[left:right+1])
            
            if nums[right] >= prev_max:
                return nums[right]
            
            if prev_max == nums[left-1]:
                return max(nums[left:right+1])
            return prev_max

        prev_max = None
        res = []
        while right < len(nums):
            maxx = (find_max(left, right, nums, prev_max))
            prev_max = maxx
            res.append(maxx)
            left+=1
            right+=1
        
        return res
        

