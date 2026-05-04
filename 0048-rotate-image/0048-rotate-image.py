class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #Soln1 using hmap to store old values
        # hmap = dict()
        # n = len(matrix)
        # for i in range(n):
        #     for j in range(n):
        #         hmap[(i,j)]=matrix[i][j]
        
        # for key,value in hmap.items():
        #     old_i=key[0]
        #     old_j=key[1]
        #     new_i = old_j
        #     new_j = (n-1-old_i)
        #     matrix[new_i][new_j]=value

        #Solution2,optimal 
        n = len(matrix)
        
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        
        for row in matrix:
            row.reverse()