class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        rows = len(grid)
        cols = len(grid[0])
        fresh_oranges =0
        queue = []
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==2:
                    queue.append((row,col,0))
                elif grid[row][col]==1:
                    fresh_oranges+=1

        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        res = 0 
        while queue:
            r,c,time = queue.pop(0)
            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                    grid[nr][nc]=2
                    fresh_oranges-=1
                    queue.append((nr,nc,time+1))
                    res= max(res,time+1)
        if fresh_oranges>0:
            return -1
        return res
        # directions = [(0,1),(1,0),(0,-1),(-1,0)]
        # res=0
        # while queue:
        #     r,c, time = queue.pop(0)
        #     for dr,dc in directions:
        #         nr,nc = r+dr, c+dc
        #         if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
        #             grid[nr][nc]=2
        #             fresh_oranges -= 1
        #             queue.append((nr,nc,time+1))
        #             res = max(res, time+1)
        # if fresh_oranges>0:
        #     return -1
        # return res