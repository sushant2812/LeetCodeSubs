class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        path = set()

        def dfs(r,c,i):
            if len(word)==i:
                return True
            if r<0 or c<0 or c>=col or r>=row or word[i]!=board[r][c] or ((r,c) in path):
                return False
            path.add((r,c))
            res = dfs(r+1,c,i+1) or dfs(r,c+1,i+1) or dfs(r-1,c,i+1) or dfs(r,c-1,i+1)
            path.remove((r,c))
            return res

        for i in range(row):
            for j in range(col):
                if dfs(i,j,0):
                    return True
        return False