class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        #Solutiuon1 (Brute Force)
        # min_cost = float("inf")
        # n = len(nums)
        # for j in range(1,n-1):
        #     for k in range(j+1,n):
        #         cost = nums[0]+nums[j]+nums[k]
        #         min_cost = min(cost, min_cost)
        # return min_cost

        #Solution 2 (Optimized using sort)
        nums[:] = [nums[0]]+ sorted(nums[1:])
        return nums[0]+nums[1]+nums[2]