class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        for num in nums:
            ans = min(ans,num)
        return ans