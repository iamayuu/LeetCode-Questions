class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #Solution 1 (using sum formula)
        n = len(nums)
        total_sum = (n*(n+1))/2
        my_sum = 0
        for n in nums:
            my_sum +=n

        return int(total_sum-my_sum)