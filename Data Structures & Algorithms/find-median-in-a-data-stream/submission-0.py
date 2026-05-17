class MedianFinder:

    def __init__(self):
        self.vals = []

    def addNum(self, num: int) -> None:
        left = 0
        right = len(self.vals)
        mid = right // 2

        while left < right:
            mid = (left + right) // 2
            if num > self.vals[mid]:
                left = mid + 1
            else:
                right = mid
        
        self.vals.insert(left, num)
        return

    def findMedian(self) -> float:
        size = len(self.vals)
        if size == 1:
            return self.vals[0]

        if size % 2 == 0:
            return (self.vals[size // 2 - 1] + self.vals[size // 2]) / 2

        return self.vals[size // 2]
 

            
        