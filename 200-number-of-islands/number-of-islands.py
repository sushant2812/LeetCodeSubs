class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        res=0
        visited =set()
        def dfs(i,j):
            if (i<0 or i>=rows) or (j<0 or j>=cols) or grid[i][j]=="0" or grid[i][j] in visited:
                return
            grid[i][j]="0"
            visited.add((i,j))
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1':
                    res+=1
                    dfs(r,c)
        return res