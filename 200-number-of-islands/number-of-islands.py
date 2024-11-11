class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        len_row = len(grid)
        len_col = len(grid[0])
        res = 0
        visited =set()
        def bfs(i,j):
            if i<0 or i>=len_row or j<0 or j>=len_col:
                return
            if (i,j) in visited or grid[i][j]!="1":
                return

            grid[i][j]="0"
            visited.add((i,j))
            bfs(i+1,j)
            bfs(i-1,j)
            bfs(i,j-1)
            bfs(i,j+1)
        for i in range(len_row):
            for j in range(len_col):
                if grid[i][j]=="1":
                    res+=1
                    bfs(i,j)
        return res