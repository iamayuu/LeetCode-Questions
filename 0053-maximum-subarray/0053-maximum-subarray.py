class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Solution1 (Brute Force) [Time Complexity - 0(n^2)]
        # max_sum = float("-inf")
        # for i in range(len(nums)):
        #     sum=0
        #     for j in range(i, len(nums)):
        #         sum+=nums[j]
        #         max_sum = max(sum,max_sum)
        # return max_sum

        #Solution2 (Kadane's Algorithm) [Time Complexity - 0(n)]
        sum = 0
        max_sum = float("-inf")
        for n in nums:
            sum = sum+n
            max_sum = max(sum,max_sum)
            if sum<0:
                sum=0
        return max_sum