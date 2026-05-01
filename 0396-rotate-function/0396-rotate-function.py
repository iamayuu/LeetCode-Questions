class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        initialSum = 0
        totalSum = 0
        n =len(nums)
        for i,num in enumerate(nums):
            initialSum += i*num
            totalSum+=num

        ans = initialSum
        for j in range(n-1,-1,-1):
            initialSum = initialSum+totalSum-(n*nums[j])
            ans = max(ans, initialSum)
        
        return ans