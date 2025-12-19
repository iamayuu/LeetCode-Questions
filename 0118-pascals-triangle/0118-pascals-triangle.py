class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows ==0:
            return [[]]
        if numRows ==1:
            return [[1]]
        if numRows ==2:
            return [[1], [1,1]]
        
        result = [[1], [1,1]]
        for i in range(2, numRows):
            arr = [1]*(i+1)
            for j in range(1,i):
                arr[j]=result[i-1][j-1]+result[i-1][j]
            result.append(arr)

        return result