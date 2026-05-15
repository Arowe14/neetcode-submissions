class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        seen = {}

        def recurse(y, x):
            if y >= m or x >= n:
                return 0

            if y == m - 1 and x == n - 1:
                return 1

            if (y, x) in seen:
                return seen[(y, x)]

            seen[(y, x)] = recurse(y + 1, x) + recurse(y, x + 1)
            return seen[(y, x)]

        return recurse(0, 0)