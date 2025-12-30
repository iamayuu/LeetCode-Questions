class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Solution1 (Brute Force) (Time - O(m*n) Space - O(m+n))
        row_zero = set()
        col_zero = set()
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    row_zero.add(i)
                    col_zero.add(j)
        for i in range(rows):
            for j in range(cols):
                if i in row_zero or j in col_zero:
                    matrix[i][j]=0

        # Solution2 (Without using extra space) (Time - O(m*n) Space - O(1))
        # firstrow_zero, firstcol_zero = False, False #Booleans to track if firstrow/firstcol already contained a zero
        # rows = len(matrix)
        # cols = len(matrix[0])
        # for i in range(rows):
        #     for j in range(cols):
        #         if i == 0 and matrix[i][j] == 0:
        #             firstrow_zero = True
        #         if j == 0 and matrix[i][j] == 0:
        #             firstcol_zero = True
        #         if i > 0 and j > 0:
        #             if matrix[i][j] == 0:
        #                 matrix[i][0] = 0
        #                 matrix[0][j] = 0
        # for i in range(1, rows):
        #     for j in range(1, cols):
        #         if matrix[i][0] == 0 or matrix[0][j] == 0:
        #             matrix[i][j] = 0
        # if firstrow_zero:
        #     matrix[0][:] = [0] * cols
        # if firstcol_zero:
        #     for i in range(rows):
        #         matrix[i][0] = 0
