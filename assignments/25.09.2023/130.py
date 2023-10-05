class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        rows=len(board)
        columns=len(board[0])
        def capture(row,col):
            if row < 0 or row > rows -1 or col < 0 or col > columns -1 or board[row][col] != "O":
                return
            board[row][col] = "T"
            capture(row-1,col)
            capture(row+1,col)
            capture(row,col-1)
            capture(row,col+1)

        
        for row in range(rows):
            for col in range(columns):
                if board[row][col] == "O":
                    if row == 0 or row == rows -1 or col == 0 or col == columns-1:
                        capture(row,col)   
        for row in range(rows):
            for col in range(columns):
                if board[row][col] != "T":
                    board[row][col] = "X"
                if board[row][col] == "T":
                    board[row][col] = "O"