class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        gridCopy = grid
        max_island = 0


        def islandSize(grid, x, y):
            grid[x][y] = 0
            island_size = 1
            if x > 0 and grid[x-1][y]==1:
                grid, size = islandSize(grid, x-1, y)
                island_size+=size
            if y > 0 and grid[x][y-1]==1:
                grid, size = islandSize(grid, x, y-1)
                island_size+=size
            if x < len(grid)-1 and grid[x+1][y]==1:
                grid, size = islandSize(grid, x+1, y)
                island_size+=size
            if y < len(grid[0])-1 and grid[x][y+1]==1:
                grid, size = islandSize(grid, x, y+1)
                island_size+=size
            return grid, island_size

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if gridCopy[i][j]==1:
                    gridCopy, island_size = islandSize(grid, i, j)
                    max_island = max(max_island, island_size)
        
        return max_island