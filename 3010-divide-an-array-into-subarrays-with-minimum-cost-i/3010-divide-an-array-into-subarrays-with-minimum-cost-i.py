class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        nums[:] = [nums[0]]+ sorted(nums[1:])
        return nums[0]+nums[1]+nums[2]