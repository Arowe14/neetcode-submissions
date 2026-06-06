class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        top_row = False # Track if top row should be set to 0s
        for r in range(rows):     # Run through each item in matrix
            for c in range(cols): # 
                if matrix[r][c] == 0:
                    if r == 0:
                        top_row = True
                    else:
                        matrix[r][0] = 0
                    matrix[0][c] = 0
        
        # Set 0s
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
        
        if top_row:
            for c in range(cols):
                matrix[0][c] = 0

        return