class Solution:
    def countSubstrings(self, s: str) -> int:
        substrings = 0

        def isPalindrome(c1, c2):
            if c1 < 0 or c2 > len(s) - 1:
                return

            nonlocal substrings
            if s[c1] == s[c2]:
                substrings += 1
                isPalindrome(c1 - 1, c2 + 1)
            
            return
        

        for i in range(len(s)):
            isPalindrome(i, i)
            isPalindrome(i, i + 1)
        
        return substrings

            
        

        


            

