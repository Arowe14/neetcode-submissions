from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {} 
        res = [] 

        # Run through words
        for word in strs:
            freq = [0] * 26
            # Get anagram array (array size 26 with each value corresponding to a letter)
            for letter in word:
                freq[ord(letter) - ord('a')] += 1
            
            freq = tuple(freq)
            # Use array as key for index in res array
            if freq not in anagrams: # Add anagram to dict, word to res
                anagrams[freq] = len(res)
                res.append([word])

            else: # Add word to res in index spot in dict
                res[anagrams.get(freq)].append(word)
        
        return res