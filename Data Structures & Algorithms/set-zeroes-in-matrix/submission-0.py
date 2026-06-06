class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])



        def findZero(r: int, c: int):
            while r < rows:
                while c < cols:
                    if matrix[r][c] == 0:
                        return r, c
                    c += 1

                c = 0
                r += 1
            
            return None, None

        def recurse(r, c):

            r, c = findZero(r, c)

            if r == None or c == None:
                return

            recurse(r, c + 1)
            if matrix[r][c] == 0:
                for i in range(cols):
                    matrix[r][i] = 0
                
                for j in range(rows):
                    matrix[j][c] = 0
            
            return
        

        return recurse(0, 0)
