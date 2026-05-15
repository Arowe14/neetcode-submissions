class Solution:
    def solve(self, board: List[List[str]]) -> None:
        x, y = len(board), len(board[0])
        unsurrounded = {}

        def dfs(i, j):
            if unsurrounded.get((i, j)):
                return
            if (i == x or i < 0 or j == y or j < 0) or board[i][j] == 'X':
                return
            
            print(i, j)
            unsurrounded[i, j] = True
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            return 
            

        # Iterate along edges
        for i in range(y):
            dfs(0, i)
            dfs(x-1, i)
        for i in range(x):
            dfs(i, 0)
            dfs(i, y-1)

        for i in range(x):
            for j in range(y):
                if board[i][j] == 'O' and not unsurrounded.get((i, j)):
                    board[i][j] = 'X'

        print(unsurrounded)
        return

