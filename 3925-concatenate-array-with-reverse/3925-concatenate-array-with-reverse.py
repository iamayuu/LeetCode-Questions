class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(nums[i])
        for i in range(len(nums)-1,-1,-1):
            ans.append(nums[i])
        return ans