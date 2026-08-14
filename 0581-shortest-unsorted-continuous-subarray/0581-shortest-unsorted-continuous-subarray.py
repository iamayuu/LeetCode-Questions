class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        l, r = 0, n-1
        while l<r:
            if nums[l]==sorted_nums[l]:
                l+=1
            elif nums[r]==sorted_nums[r]:
                r-=1
            else:
                break
        
        return 0 if r==l else (r-l+1)