class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #Variable Size Sliding Window
        n = len(nums)
        l , r = 0,0
        crrSum = nums[0]
        minLen = float("inf")
        while l<=r:
            if crrSum>=target:
                minLen = min(minLen, (r-l+1))
                crrSum-=nums[l]
                l+=1
                
            elif r<n-1:
                r+=1
                crrSum+=nums[r]
            else:
                break
        return 0 if minLen==float("inf") else minLen