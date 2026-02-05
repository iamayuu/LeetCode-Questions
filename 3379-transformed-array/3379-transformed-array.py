class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        for i in range(n):
            if nums[i]==0:
                result.append(nums[i])
            else:
                result.append(nums[(i+nums[i])%n])
        return result