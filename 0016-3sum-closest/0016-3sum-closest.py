class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        min_diff, ans = float("inf"), float("inf")
        for i in range(n-2):
            l=i+1
            r = n-1
            while l<r:
                sum = nums[i]+nums[l]+nums[r]
                if sum == target:
                    return sum
                else:
                    diff = abs(sum-target)
                    if diff < min_diff:
                        min_diff = diff
                        ans = sum
                    if sum<target:
                        l+=1
                    else:
                        r-=1
            
        return ans


