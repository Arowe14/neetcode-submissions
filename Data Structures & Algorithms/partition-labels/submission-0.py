class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {}
        idx = 0
        for ch in s:
            last_idx[ch] = idx
            idx+=1

        size = 0
        idx=0
        end = 0
        out = []
        for ch in s:
            end = max(end, last_idx[ch])
            size+=1
            idx+=1
            print(end, idx)
            if idx>end:
                out.append(size)
                size=0
        
        return out
