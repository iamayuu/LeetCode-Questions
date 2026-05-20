class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        #Solution 1 
        # n = len(A)
        # arr = [0]*n
        # for i in range(n):
        #     num = A[i]
        #     j = B.index(num) 
        #     arr[max(i,j)]+=1
        
        # for i in range(1,n):
        #     arr[i]+=arr[i-1]

        # return arr

        #Solution 2
        seen = set()
        n = len(A)
        arr = [0]*n
        for i in range(n):
            if A[i] in seen:
                arr[i]+=1
            if B[i] in seen:
                arr[i]+=1
            if A[i]==B[i]:
                arr[i]+=1

            seen.add(A[i])
            seen.add(B[i])
        
        for i in range(1,n):
            arr[i]+=arr[i-1]
        
        return arr