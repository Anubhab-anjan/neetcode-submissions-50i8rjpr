class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        row = [set()for _ in range(9)]
        column = [set()for _ in range(9)]
        squares= [set()for _ in range(9)]
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                box_index = (r//3)*3+(c//3)
                if (val in row[r]) or (val in column[c]) or (val in squares[box_index]):
                    return False
                row[r].add(val)
                column[c].add(val)
                squares[box_index].add(val)
        
        return True
