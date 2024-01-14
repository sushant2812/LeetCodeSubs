class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        top = 0
        bottom = rows - 1
        while top <= bottom:
            row = (top + bottom)//2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix [row][0]:
                bottom = row -1
            else:
                break
        if not(top<=bottom):
            return False
        row = (top+bottom)//2
        l = 0
        r = cols -1
        while l<=r:
            num=(l+r)//2
            if matrix[row][num]==target:
                return True
            elif matrix[row][num]>target:
                r=num-1
            elif matrix[row][num]<target:
                l=num+1
        return False