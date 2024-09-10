class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=collections.defaultdict(set)
        columns=collections.defaultdict(set)
        squares=collections.defaultdict(set)
        for row in range(9):
            for col in range(9):
                
                ## Checking for the presence of a non-unique number

                if board[row][col]=='.':
                    continue
                if board[row][col] in rows[row]:
                    return False
                if board[row][col] in columns[col]:
                    return False
                if board[row][col] in squares[(row//3,col//3)]:
                    return False
                
                ## Adding to the set

                rows[row].add(board[row][col])
                columns[col].add(board[row][col])
                squares[(row//3,col//3)].add(board[row][col])

        return True