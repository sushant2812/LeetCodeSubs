class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def dfs(i, j):
            board[i][j] = 'Y'
            for x, y in directions:
                ix, jy = i + x, j + y
                if 0 <= ix < m and 0 <= jy < n and board[ix][jy] == 'O':
                    dfs(ix, jy)
        
        # Traverse borders to find 'O's
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    if board[i][j] == 'O':
                        dfs(i, j)
        
        # Replace all 'O's with 'X's
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        
        # Replace all 'Y's back to 'O's
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'Y':
                    board[i][j] = 'O'