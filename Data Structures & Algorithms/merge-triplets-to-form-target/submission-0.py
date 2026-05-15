class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [0, 0, 0]

        def checkTuple(triplet: List[int]) -> List[int] | None:
            for i in range(3):
                if triplet[i] > target[i]:
                    return
            
            return triplet


        for triplet in triplets:
            t = checkTuple(triplet)
            if t:
                res = [max(res[0], t[0]), max(res[1], t[1]), max(res[2], t[2])]
            if res == target:
                return True
        return False










            
            