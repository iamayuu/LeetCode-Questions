class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        #Solution1 - Brute Force - T.L.E.
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

        #Solution 2 - Optimization using D.A.T.
        # n = len(nums)
        # arr = [0]*((2*limit)-1)
        # m = len(arr)
        # arr[0]=n
        # for i in range(n//2):
        #     a = nums[i]
        #     b = nums[n-1-i]
        #     minOf1Move = min(a,b)+1
        #     maxOf1Move = max(a,b)+limit
        #     arr[minOf1Move-2]-=1
        #     if (maxOf1Move-1)<m:
        #         arr[maxOf1Move-1]+=1
        #     arr[a+b-2]-=1
        #     if (a+b-1)<m:
        #         arr[a+b-1]+=1
        
        # ans = arr[0]
        
        # for i in range(1,m):
        #     arr[i]=arr[i-1]+arr[i]
        #     ans = min(ans,arr[i])

        # return ans

        #Clean code of solution 2
        n = len(nums)
        arr = [0]*((2*limit)+1)
        arr[2]=n
        m=len(arr)
        for i in range(n//2):
            a = nums[i]
            b = nums[n-1-i]
            low = min(a,b)+1
            high = max(a,b)+limit
            exact = a+b

            arr[low] -= 1
            if high+1<m:
                arr[high+1] += 1

            arr[exact] -= 1
            if exact+1<m:
                arr[exact+1] += 1

        ans =float("inf")

        mini = 2
        maxi = 2*limit
        curr = 0
        for i in range(mini,maxi+1):
            curr+=arr[i]
            ans = min(ans,curr)

        return ans


