class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        arr = [0]*n
        for i in range(n):
            num = A[i]
            j = B.index(num) 
            arr[max(i,j)]+=1
        
        for i in range(1,n):
            arr[i]+=arr[i-1]

        return arr