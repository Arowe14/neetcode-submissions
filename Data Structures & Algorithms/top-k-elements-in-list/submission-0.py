import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        heap = []
        res = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            heapq.heappush(heap, [-c, n])
        
        for i in range(k):
            n = heapq.heappop(heap)[1]
            res.append(n)
        
        return res
