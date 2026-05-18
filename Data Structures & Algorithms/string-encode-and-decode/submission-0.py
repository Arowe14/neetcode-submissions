class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s))
            encoded += str("#")
            encoded += s

        return encoded

    def decode(self, s: str) -> List[str]:
        length = 0
        i = 0
        decoded = []

        while i < len(s):
            if s[i].isdigit():
                length *= 10
                length += int(s[i])

            elif s[i] == "#":
                decoded.append(s[i + 1 : i + length + 1])
                i += length
                length = 0

            i += 1
        
        return decoded
            

            

            
