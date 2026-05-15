class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        #Brute Force - T.L.E.
        # n = len(nums)
        # minTarget = 2
        # maxTarget = 2*limit
        # ans = float("inf") #minimum moves
        
        # def movesReq(target,a,b):
        #     if a+b==target:
        #         return 0
        #     if target>=(min(a,b)+1) and target<=(max(a,b)+limit):
        #         return 1
        #     return 2

        # for target in range(minTarget, maxTarget+1):
        #     moves = 0
        #     for i in range(n//2):
        #         a = nums[i]
        #         b = nums[n-1-i]
        #         moves+= movesReq(target,a,b)

        #     ans=min(ans,moves)

        # return ans

        #Optimization using D.A.T.
        def movesReq(target,a,b):
            if a+b==target:
                return 0
            if target>=(min(a,b)+1) and target<=(max(a,b)+limit):
                return 1
            return 2
        n = len(nums)
        arr = [0]*((2*limit)-1)
        m = len(arr)
        arr[0]=n
        for i in range(n//2):
            a = nums[i]
            b = nums[n-1-i]
            minOf1Move = min(a,b)+1
            maxOf1Move = max(a,b)+limit
            arr[minOf1Move-2]-=1
            if (maxOf1Move-1)<m:
                arr[maxOf1Move-1]+=1
            arr[a+b-2]-=1
            if (a+b-1)<m:
                arr[a+b-1]+=1
        
        ans = arr[0]
        
        for i in range(1,m):
            arr[i]=arr[i-1]+arr[i]
            ans = min(ans,arr[i])

        return ans

