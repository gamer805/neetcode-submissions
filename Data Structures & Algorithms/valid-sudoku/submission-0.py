class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            row_dict = {}
            for num in row:
                row_dict[num] = 1 + row_dict.get(num, 0)
                if row_dict[num] > 1 and num != ".": return False
        for i in range(9):
            col_dict = {}
            for row in board:
                col_dict[row[i]] = 1 + col_dict.get(row[i], 0)
                if col_dict[row[i]] > 1 and row[i] != ".": return False

        for i in range(9):
            first_row = 3*int(i/3)
            first_col = 3*(i%3)
            sub = board[first_row][first_col:first_col+3] + board[first_row+1][first_col:first_col+3] + board[first_row+2][first_col:first_col+3]
            sub_dict = {}
            for num in sub:
                sub_dict[num] = 1 + sub_dict.get(num, 0)
                if sub_dict[num] > 1 and num != ".": return False
        
        return True