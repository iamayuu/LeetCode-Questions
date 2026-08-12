class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        my_set = set()
        ans = []
        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            crr_target = target-nums[i]
            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                l = j+1
                r = n-1
                while l<r:
                    crr_sum = nums[j]+nums[l]+nums[r]
                    if crr_sum == crr_target:
                        tp = tuple([nums[i],nums[j],nums[l],nums[r]])
                        if tp not in my_set:
                            ans.append([nums[i],nums[j],nums[l],nums[r]])
                            my_set.add(tp)
                        l+=1
                        r-=1
                    elif crr_sum < crr_target:
                        l+=1
                    else:
                        r-=1
        return ans