class Solution:
    def longestPalindrome(self, s: str) -> str:
        currmax = ""

        def palindrome(l, r):
            check = ""
            while l >= 0 and r < len(s) and s[l] == s[r]:
                check = s[l:r+1]
                l -= 1
                r += 1

            return check if len(check) > len(currmax) else currmax

        for i in range(len(s)):
            currmax = palindrome(i, i)
            currmax = palindrome(i, i + 1)
        
        return currmax