class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        #Solution1
        # result = []
        # n = len(nums)
        # for i in range(n):
        #     if nums[i]==0:
        #         result.append(nums[i])
        #     else:
        #         result.append(nums[(i+nums[i])%n])
        # return result

        #Solution2
        # result = []
        # n = len(nums)
        # for i in range(n):
        #     result.append(nums[(i+nums[i])%n])
        # return result

        #Solution 3
        n = len(nums)
        return [nums[(i+nums[i])%n] for i in range(n)]