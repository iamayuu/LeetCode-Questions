class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        zeroes = [] #List to track the zeroes from right side in each row
        for row in grid:
            count_zeroes = 0
            for value in row[::-1]:
                if value == 0:
                    count_zeroes+=1
                else:
                    break
            zeroes.append(count_zeroes)

        #Now we will find zeroes needed for every row, and 
        #then if we get any value more then our required amount then we will have a swap
        total_swaps = 0

        for row_idx in range(n):
            need = (n-row_idx-1) #Min zeroes needed for (row_idx+1)'th row i.e. 1st Row (idx=0) will need n-1
            j = row_idx #Index starting from row's index to iterate in zeroes list
            while j<n:
                if zeroes[j] >= need:
                    break
                j+=1

            if j==n:
                return -1
            
            #If we found the j we needed, then we will simulate the swap from row_idx to j
            while j != row_idx:
                zeroes[j], zeroes[j-1]=zeroes[j-1],zeroes[j]
                j-=1
                total_swaps+=1

        return total_swaps
            