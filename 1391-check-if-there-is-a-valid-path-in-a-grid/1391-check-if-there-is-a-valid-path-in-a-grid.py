class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        valid_entry =   {
                            1: [[0,-1],[0,1]],
                            2: [[-1,0],[1,0]],
                            3: [[0,-1], [1,0]],
                            4: [[0,1], [1,0]],
                            5: [[-1,0],[0,-1]],
                            6: [[-1,0], [0,1]]
                        }

        def is_valid(cell):
            i,j = cell[0], cell[1]
            if i<0 or j<0 or i>=m or j>=n:
                return False
            return True

        def is_validmove(i, j, next_cell):
            a, b = next_cell[0], next_cell[1]
            nextCellType = grid[a][b]
            prev_cells = valid_entry[nextCellType]
            if a+prev_cells[0][0]==i and b+prev_cells[0][1]==j:
                return True
            elif a+prev_cells[1][0]==i and b+prev_cells[1][1]==j:
                return True
            else:
                return False
            

        m = len(grid)
        n = len(grid[0])
        visited_cell = [[False]*n for _ in range(m)]

        i, j = 0, 0
        def dfs(i,j):
            if i==m-1 and j==n-1:
                return True

            crr_type = grid[i][j]
            visited_cell[i][j]=True

            next_cells = valid_entry[crr_type]
            
            #dx and dy are +-1 or 0 from valid_entry map, and this loop will run for 2 times exploring both path for cell
            for dx,dy in next_cells:
                ni, nj = i+dx, j+dy
                next_cell = [ni, nj]
                if is_valid(next_cell) and visited_cell[ni][nj]==False and is_validmove(i, j, next_cell):
                    if dfs(ni, nj):
                        return True
            
            return False
        
        return dfs(0,0)
