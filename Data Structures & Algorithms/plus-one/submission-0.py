class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = digits
        

        for i in range(len(digits) - 1, - 1, -1):
            res[i] += 1
            if res[i] < 10:
                break
            res[i] = 0
            
        if res[0] == 0:
            res.insert(0, 1)
        
        return res