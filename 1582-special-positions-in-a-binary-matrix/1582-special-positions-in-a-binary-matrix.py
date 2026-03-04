class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        #Solution1 (Brute Force)
        m = len(mat)
        n = len(mat[0])
        count=0
        for row in range(m):
            for col in range(n):
                if mat[row][col]==1:
                    row_check = True
                    col_check = True
                    for i in range(n):
                        if mat[row][i]==1 and i!=col:
                            row_check  = False
                            break
                    for j in range(m):
                        if mat[j][col]==1 and j!=row:
                            col_check  = False
                            break
                    if row_check and col_check:
                        count+=1
        return count
                        