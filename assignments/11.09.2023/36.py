class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
          if not is_valid(row):
            return False

   
        for col in zip(*board):
          if not is_valid(col):
            return False

        for i in range(0, 9, 3):
          for j in range(0, 9, 3):
            subgrid = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not is_valid(subgrid):
              return False

        return True

def is_valid(nums):
    seen = set()
    for num in nums:
        if num != ".":
            if num in seen:
                return False
            seen.add(num)
    return True
