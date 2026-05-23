class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        t, b = 0, ROWS - 1
        m = 0

        while t <= b:
            m = (b + t) // 2
            
            if matrix[m][0] > target:
                b = m - 1
            
            elif matrix[m][-1] < target:
                t = m + 1
            
            else:
                break

        if not t <= b:
            return False

        row = matrix[(t + b) // 2]
        l, r = 0, COLS - 1

        while l <= r:
            m = (r + l) // 2

            if row[m] > target:
                r = m - 1
            
            elif row[m] < target:
                l = m + 1
            
            else:
                return True
        
        return False

        