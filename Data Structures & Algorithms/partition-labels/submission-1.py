class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {}
        for i, c in enumerate(s):
            last_idx[c] = i

        size = 0
        end = 0
        out = []
        for i, c in enumerate(s):
            end = max(end, last_idx[c])
            size+=1
            if i==end:
                out.append(size)
                size=0
        
        return out
