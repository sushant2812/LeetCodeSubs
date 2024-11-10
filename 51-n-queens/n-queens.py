class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag= set()
        negDiag = set()
        board = [['.']*n for i in range(n)]
        res=[]
        def backtrack(r):
            if r==n:
                res.append([''.join(row) for row in board])
                return
            for c in range(n):
                if c in col or (r+c in posDiag) or (r-c in negDiag):
                    continue
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c]='Q'
                backtrack(r+1)
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c]='.'
        backtrack(0)   
        print(res)
        return res


        ## ur just placing queens at different points and seeing what sticks. thats why res>1