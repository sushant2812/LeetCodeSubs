
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        board = [[0] * n for _ in range(m)] # 0: unguarded, 1: guarded, -1: wall/guard
        for x, y in walls:
            board[x][y] = -1
        for x, y in guards:
            board[x][y] = -1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] 
        queue = deque(guards)
        while queue:
            x,y = queue.popleft()
            for dx,dy in directions:
                nx,ny = x+dx, y+dy
                while 0<=nx<m and 0<=ny<n:
                    if board[nx][ny]==-1:
                        break
                    if board[nx][ny]==0:
                        board[nx][ny]=1
                    nx,ny=nx+dx,ny+dy
        unguarded_count = sum(1 for i in range(m) for j in range(n) if board[i][j] == 0)
        return unguarded_count