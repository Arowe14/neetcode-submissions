class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        letters1 = [0] * 26
        letters2 = [0] * 26
        
        for i, letter in enumerate(s1):
            letters1[ord(letter) - ord('a')] += 1
            letters2[ord(s2[i]) - ord('a')] += 1
        
        l, r = 0, len(s1) - 1
        while r < len(s2) - 1:
            if letters1 == letters2:
                return True

            letters2[ord(s2[l]) - ord('a')] -= 1

            l += 1
            r += 1
            letters2[ord(s2[r]) - ord('a')] += 1

        
        return letters1 == letters2