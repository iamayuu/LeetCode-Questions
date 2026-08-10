class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        min_diff, ans = float("inf"), nums[0]+nums[1]+nums[2]
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r = n-1
            while l<r:
                crr_sum = nums[i]+nums[l]+nums[r]
                if crr_sum == target:
                    return crr_sum
                else:
                    diff = abs(crr_sum-target)
                    if diff < min_diff:
                        min_diff = diff
                        ans = crr_sum
                    if crr_sum<target:
                        l+=1
                    else:
                        r-=1
            
        return ans


