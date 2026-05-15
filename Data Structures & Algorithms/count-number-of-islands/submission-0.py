class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        gridCopy = grid
        islands = 0


        def foundIsland(grid: List[List[str]], x: int, y: int) -> List[List[str]]:
            grid[x][y] = "0"
            if x > 0 and grid[x-1][y]=="1":
                grid = foundIsland(grid, x-1, y)
            if y > 0 and grid[x][y-1]=="1":
                grid = foundIsland(grid, x, y-1)
            if x < len(grid)-1 and grid[x+1][y]=="1":
                grid = foundIsland(grid, x+1, y)
            if y < len(grid[0])-1 and grid[x][y+1]=="1":
                grid = foundIsland(grid, x, y+1)

            return grid

          
        for x in range(len(gridCopy)):
            for y in range(len(gridCopy[0])):
                if gridCopy[x][y]=="1":
                    islands+=1
                    gridCopy = foundIsland(gridCopy, x, y)




        

        return islands
