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
        # seen = set()
        # n = len(A)
        # arr = [0]*n
        # for i in range(n):
        #     if A[i] in seen:
        #         arr[i]+=1
        #     if B[i] in seen:
        #         arr[i]+=1
        #     if A[i]==B[i]:
        #         arr[i]+=1

        #     seen.add(A[i])
        #     seen.add(B[i])
        
        # for i in range(1,n):
        #     arr[i]+=arr[i-1]
        
        # return arr

        #Solution 3
        n = len(A)
        maskA , maskB = 0, 0
        arr = []
        def totalSetBits(n):
            count=0
            while n!=0:
                n = n&(n-1)
                count+=1

            return count

        for i in range(n):
            maskA = maskA | (1<<A[i])
            maskB = maskB | (1<<B[i])

            final = maskA & maskB

            arr.append(totalSetBits(final))
        
        return arr
