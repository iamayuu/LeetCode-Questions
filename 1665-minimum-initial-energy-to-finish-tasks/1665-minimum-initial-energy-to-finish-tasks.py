class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        #Solution 1 Binary Search + Custom Sorting
        # def isPossible(mid, tasks):
        #     for task in tasks:
        #         if mid>=task[1]:
        #             mid = mid-task[0]
        #         else:
        #             return False
        #     return True

        # tasks.sort(key = lambda x:x[1]-x[0], reverse = True)

        # l = 0
        # r = 10**9
        # ans = float("inf")
        # while l<=r:
        #     mid = (r+l)//2
        #     if isPossible(mid, tasks):
        #         ans = min(ans,mid)
        #         r = mid-1
        #     else:
        #         l=mid+1
        
        # return ans

        #Solutuion 2 Greedy
        tasks.sort(key = lambda x:x[1]-x[0], reverse = True)
        currEnergy = 0
        minTotal = 0
        for task in tasks:
            actual = task[0]
            minimum = task[1] 
            if currEnergy<minimum:
                extra  = minimum-currEnergy
                minTotal+=extra
                currEnergy=currEnergy+extra
                currEnergy=currEnergy-actual
            else:
                currEnergy=currEnergy-actual

        return minTotal

