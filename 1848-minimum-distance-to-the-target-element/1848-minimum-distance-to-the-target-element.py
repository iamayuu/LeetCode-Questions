class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        #Solution1 Brute Force
        ans = float("inf")
        dist = 0
        for i in range(len(nums)):
            if nums[i]==target:
                dist = abs(i-start)
                ans = min(ans, dist)
                if ans==0:
                    return ans
        return ans