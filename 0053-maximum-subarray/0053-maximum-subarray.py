class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        crr_sum = 0
        for num in nums:
            crr_sum += num
            max_sum = max(crr_sum,max_sum)
            if crr_sum < 1:
                crr_sum=0
        return max_sum