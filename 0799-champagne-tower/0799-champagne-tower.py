#Solution 1
# def total_champagne(poured, i, j, memo):

#     if i < 0 or j < 0 or i < j:
#         return 0.0

#     if memo[i][j] != -1:
#         return memo[i][j]

#     if i == 0 and j == 0:
#         memo[i][j] = poured
#         return poured

#     up_left = (total_champagne(poured, i - 1, j - 1, memo) - 1) / 2
#     up_right = (total_champagne(poured, i - 1, j, memo) - 1) / 2

#     if up_left < 0:
#         up_left = 0
#     if up_right < 0:
#         up_right = 0

#     memo[i][j] = up_left + up_right
#     return memo[i][j]


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        #Solution 1 (using recursion)
        # memo = [[-1 for _ in range(query_row + 1)] 
        #         for _ in range(query_row + 1)]
        
        # return min(1.0, total_champagne(poured, query_row, query_glass, memo))

        #Solurion 2 (Using DP)
        T = [[0.0] * 101 for _ in range(101)]
        T[0][0] = float(poured)

        for row in range(query_row + 1):
            for col in range(row + 1):
                extra = (T[row][col] - 1.0) / 2.0
                if extra > 0:
                    T[row + 1][col] += extra
                    T[row + 1][col + 1] += extra

        return min(1.0, T[query_row][query_glass])
