class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        min_cost = nums[0]
        nums[:] = sorted(nums[1:])
        return min_cost+nums[0]+nums[1]