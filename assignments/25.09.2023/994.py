class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        stack=[]
        rows=len(grid)
        cols=len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    stack.append([i,j])
        result=-1
        while stack:
            temp=stack.copy()
            stack.clear()
            for i, j in temp:
                if i-1>=0 and grid[i-1][j]==1:
                    stack.append([i-1,j])
                    grid[i-1][j]=2
                if i+1<rows and grid[i+1][j]==1:
                    stack.append([i+1,j])
                    grid[i+1][j]=2
                if j-1>=0 and grid[i][j-1]==1:
                    stack.append([i,j-1])
                    grid[i][j-1]=2
                if j+1<cols and grid[i][j+1]==1:
                    stack.append([i,j+1])
                    grid[i][j+1]=2
                grid[i][j]=2
            result+=1

        for i in grid:
            for j in i:
                if j==1:
                    return -1
        return result if result>=0 else 0
