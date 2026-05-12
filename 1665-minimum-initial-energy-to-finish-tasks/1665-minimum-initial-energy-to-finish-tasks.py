class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        def isPossible(mid, tasks):
            for task in tasks:
                if mid>=task[1]:
                    mid = mid-task[0]
                else:
                    return False
            return True

        tasks.sort(key = lambda x:x[1]-x[0], reverse = True)

        l = 0
        r = 10**9
        ans = float("inf")
        while l<=r:
            mid = (r+l)//2
            if isPossible(mid, tasks):
                ans = min(ans,mid)
                r = mid-1
            else:
                l=mid+1
        
        return ans