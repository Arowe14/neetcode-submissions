class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        repeats = set()
        subset = 1

        l, r = 0, 1
        repeats.add(s[l])

        while r < len(s):
            if s[r] in repeats:
                while s[l] != s[r]:
                    repeats.remove(s[l])
                    l += 1
                l += 1
            
            else:
                repeats.add(s[r])
            
            subset = max(subset, len(repeats))
            r += 1
        
        return subset