class Solution:
    def climbStairs(self, n: int) -> int:
        ways = {}

        ways[1] = 1
        ways[2] = 2

        def recurse(x):
            if x < 1:
                return 0
            if ways.get(x):
                return ways[x]
            
            ways[x] = recurse(x-1) + recurse(x-2)
            return ways[x]

        return recurse(n)
