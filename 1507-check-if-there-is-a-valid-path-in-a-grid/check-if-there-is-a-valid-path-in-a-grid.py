class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        seen = {(0, 0)}
        queue = deque([(0, 0)])
        n = len(grid)
        m = len(grid[0])

        # 1 which means a street connecting the left cell and the right cell. [(0, 1), (0, -1)]
        # 2 which means a street connecting the upper cell and the lower cell. [(-1, 0), (1, 0)]
        # 3 which means a street connecting the left cell and the lower cell.  [(1, 0), (0, -1)]
        # 4 which means a street connecting the right cell and the lower cell.  [(1, 0), (0, 1)]
        # 5 which means a street connecting the left cell and the upper cell. [(-1,0),(0,-1)]
        # 6 which means a street connecting the right cell and the upper cell. [(0,1),(-1,0)]
        # return valid path from (0,0) to (n-1,n-1)

        directions = {
            1: [(0, 1), (0, -1)],  
            2: [(-1, 0), (1, 0)],  
            3: [(1, 0), (0, -1)],  
            4: [(1, 0), (0, 1)],  
            5: [(0, -1), (-1, 0)],  
            6: [(0, 1), (-1, 0)],  
        }  # the rule is connected -dx,-dy

        while queue:
            row, col = queue.popleft()

            if (row, col) == (n - 1, m - 1):
                return True

            for dx, dy in directions[grid[row][col]]:
                row_, col_ = row + dx, col + dy
                if 0 <= row_ < n and 0 <= col_ < m and (row_, col_) not in seen:
                    if (-dx,-dy) in directions[grid[row_][col_]]:
                        queue.append((row_, col_))
                        seen.add((row_, col_))

        return False