class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        start_row = 0
        end_row = len(matrix)-1
        start_col = 0
        end_col = len(matrix[0])-1
        result = []
        while start_row<=end_row and start_col<=end_col:
            #Adding Top Boundary
            for j in range(start_col, end_col+1):
                result.append(matrix[start_row][j])
            #Adding Right Boundary
            for j in range(start_row+1, end_row+1):
                result.append(matrix[j][end_col])
            #Adding Bottom Boundary
            for j in range(end_col-1, start_col-1, -1):
                if start_row==end_row:
                    break
                result.append(matrix[end_row][j])
            #Adding Left Boundary
            for j in range(end_row-1, start_row, -1):
                if start_col==end_col:
                    break
                result.append(matrix[j][start_col])
            start_row+=1
            end_row-=1
            start_col+=1
            end_col-=1
        return result
