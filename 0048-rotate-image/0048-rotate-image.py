class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #Solution 1 (Time - O(n^2) and Using extra space O(n^2))
        # n=len(matrix)
        # result = [[0 for x in range(n)] for y in range(n)]
        # for i in range(n):
        #     for j in range(n):
        #         result[j][n-1-i]=matrix[i][j]
        # matrix[:]=result

        #Solution 2 (Transpose Matrix) (Without using extra space) (Time - 0(n^2) Space - O(1))
        n=len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i]=matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i]=matrix[i][::-1]
            

        