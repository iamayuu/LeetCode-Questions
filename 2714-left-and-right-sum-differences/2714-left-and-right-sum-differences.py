class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        #Brute Force
        # leftsum, rightsum = [], []
        # n = len(nums)
        # left, right = 0, 0
        # for i in range(1,n):
        #     leftsum.append(left+nums[i-1])
        #     rightsum.append(right+nums[n-i])
        #     left+=nums[i-1]
        #     right+=nums[n-i]

        # leftsum = [0]+leftsum
        # rightsum = rightsum[::-1]+[0]

        # ans = []
        # for i in range(n):
        #     ans.append(abs(leftsum[i]-rightsum[i]))
        # return ans

        #Optimized
        #rightsum[i] = totalsum - num[i]
        leftsum = 0
        rightsum = sum(nums)

        ans = []

        for num in nums:
            rightsum = rightsum - num
            ans.append(abs(rightsum-leftsum))
            leftsum = leftsum+num

        return ans