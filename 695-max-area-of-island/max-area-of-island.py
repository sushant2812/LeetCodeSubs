class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area=0
        rows=len(grid)
        cols=len(grid[0])
        def dfs(i,j):
            if i<0 or i>=rows or j<0 or j>=cols or grid[i][j]!=1:
                return 0
            grid[i][j]=0
            area=1
            area+=dfs(i+1,j)
            area+=dfs(i-1,j)
            area+=dfs(i,j+1)
            area+=dfs(i,j-1)
            return area
        for r in range(rows):
            for c in range(cols):
                max_area=max(max_area,dfs(r,c))
        return max_area