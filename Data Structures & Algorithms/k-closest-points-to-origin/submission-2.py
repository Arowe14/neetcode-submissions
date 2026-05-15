import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        nheap = []
        
        for point in points:
            distance = math.sqrt((point[0]**2) + (point[1]**2))
            
            if len(nheap) < k:
                heapq.heappush(nheap, ((distance * -1), point))
            else:
                if (distance * -1) > nheap[0][0]:
                    heapq.heappushpop(nheap, ((distance * -1), point))
        
        return [item[1] for item in nheap]