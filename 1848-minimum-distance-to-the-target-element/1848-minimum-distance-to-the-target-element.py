class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        #Solution1 Brute Force
        # ans = float("inf")
        # dist = 0
        # for i in range(len(nums)):
        #     if nums[i]==target:
        #         dist = abs(i-start)
        #         ans = min(ans, dist)
        #         if ans==0:
        #             return ans
        # return ans

        #Soltion2 (2 pointers)
        left=start
        right=start
        ans = float("inf")
        while left>=0:
            if nums[left]==target:
                ans = min(ans, abs(left-start))
                break
            left-=1

        while right<len(nums):
            if nums[right]==target:
                ans = min(ans, abs(right-start))
                break
            right+=1
        return ans