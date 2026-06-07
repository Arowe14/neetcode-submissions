class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)

        for i in range(n + 1):
            num = i
            while num:
                res[i] += 1 if num & 1 else 0
                num >>= 1
        
        return res
