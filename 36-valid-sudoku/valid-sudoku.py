class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=collections.defaultdict(set)
        cols=collections.defaultdict(set)
        squares=collections.defaultdict(set)
        for row in range(9):
            for col in range(9):
                number=board[row][col]
                if number == '.':
                    continue
                if number in rows[row] or number in cols[col] or number in squares[(row//3,col//3)]:
                    return False
                rows[row].add(number)
                cols[col].add(number)
                squares[(row//3,col//3)].add(number)
        return True