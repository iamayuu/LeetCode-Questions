class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        totalArea  = 0
        maxRowArea = [0]*n
        maxColArea = [0]*n
        
        for i in range(n):
            for j in range(n):
                if grid[i][j]!=0:
                    totalArea+=1
                    if maxColArea[j]<grid[i][j]:
                        maxColArea[j]=grid[i][j]
                    if maxRowArea[i]<grid[i][j]:
                        maxRowArea[i]=grid[i][j]
        totalArea+=sum(maxRowArea)+sum(maxColArea)
        return totalArea
