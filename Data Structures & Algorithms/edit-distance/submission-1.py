class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = {}
        def recurse(i: int, j: int) -> int:
            if i == len(word1):
                return len(word2) - j
            
            if j == len(word2):
                return len(word1) - i
            
            if word1[i] == word2[j]:
                print(i, j)
                return recurse(i + 1, j + 1)

            if (i, j) in dp:
                return dp[(i, j)]
                
            res = min(
                recurse(i, j + 1), # Insert
                recurse(i + 1, j), # Delete 
                recurse(i + 1, j + 1) # Replace
            )
            dp[(i, j)] = 1 + res
            return dp[(i, j)]
        
        return recurse(0, 0)