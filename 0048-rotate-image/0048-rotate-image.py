class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        hmap = dict()
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                hmap[(i,j)]=matrix[i][j]
        
        for key,value in hmap.items():
            old_i=key[0]
            old_j=key[1]
            new_i = old_j
            new_j = (n-1-old_i)
            matrix[new_i][new_j]=value