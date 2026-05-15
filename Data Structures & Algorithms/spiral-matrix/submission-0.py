class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        minx, miny = 0, 0
        maxx, maxy = len(matrix[0]), len(matrix)

        spiral = []

        while (minx < maxx and miny < maxy):
            print("START")

            for top in range(minx, maxx): # Top Side
                print("TOP: ", matrix[miny][top])
                spiral.append(matrix[miny][top])
            
            if miny + 1 == maxy: # If current section is just a row, stop
                break

            for right in range(miny + 1, maxy): # Right Side
                print("RIGHT: ", matrix[right][maxx - 1])
                spiral.append(matrix[right][maxx - 1])

            if minx + 1 == maxx: # If current section is just a column, stop
                break
            
            for bottom in range(maxx - 2, minx - 1, -1): # Bottom Side
                print("BOTTOM: ", matrix[maxy - 1][bottom])
                spiral.append(matrix[maxy - 1][bottom])

            for left in range(maxy - 2, miny, -1): # Left Side
                print("LEFT: ", matrix[left][minx])
                spiral.append(matrix[left][minx])

            minx += 1
            miny += 1
            maxx -= 1
            maxy -= 1

        return spiral