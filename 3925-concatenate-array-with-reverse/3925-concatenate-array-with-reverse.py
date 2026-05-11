class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    continue
            ans.append(nums[i])
        for i in range(len(nums)-1,-1,-1):
            ans.append(nums[i])
        return ans