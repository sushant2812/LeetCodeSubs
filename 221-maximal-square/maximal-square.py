class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows=len(matrix)
        cols=len(matrix[0])
        cache={}
        def helper(r,c):
            if r>=rows or r<0 or c>=cols or c<0:
                return 0
            if (r,c) not in cache:
                down=helper(r+1,c)
                right=helper(r,c+1)
                diag=helper(r+1,c+1)
                cache[(r,c)]=0
                if matrix[r][c]=="1":
                    cache[(r,c)]= 1+ min(down,diag,right)
            return cache[(r,c)]

        helper(0,0)
        return max(cache.values())**2