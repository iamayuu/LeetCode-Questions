class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #Solution 1 (Usin extra space O(n^2))
        n=len(matrix)
        result = [[0 for x in range(n)] for y in range(n)]
        for i in range(n):
            for j in range(n):
                result[j][n-1-i]=matrix[i][j]
        matrix[:]=result

        