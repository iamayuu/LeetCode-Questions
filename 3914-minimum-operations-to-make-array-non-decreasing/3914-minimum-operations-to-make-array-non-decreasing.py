class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        x = 0
        for i in range(1,n):
            if nums[i]<nums[i-1]:
                x+= nums[i-1]-nums[i]
        return x