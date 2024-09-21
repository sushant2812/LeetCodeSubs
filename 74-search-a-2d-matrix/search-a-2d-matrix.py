class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top=0
        bottom=len(matrix)-1
        while top<=bottom:
            row = (top+bottom)//2
            if target>matrix[row][-1]: ## Bigger than the last element of the row
                top = row+1
            elif target<matrix[row][0]:
                bottom=row-1
            else:
                break ##Right Row!
        if not(top<=bottom):
            return False ##Nothin
        row = (top+bottom)//2
        left = 0
        print(row)
        right = len(matrix[0])-1
        while left<=right:
            mid = (left+right)//2
            if matrix[row][mid]==target:
                return True
            if matrix[row][mid]>target:
                right=mid-1
            else:
                left=mid+1
        return False
