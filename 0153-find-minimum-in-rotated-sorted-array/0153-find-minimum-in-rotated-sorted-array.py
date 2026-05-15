class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if len(nums)<=2:
        #     return min(nums)
        # l = 0 
        # r = len(nums)-1
        # while l<=r:
        #     m = (l+r)//2
        #     if nums[m-1]>nums[m] and nums[m+1]>nums[m]:
        #         return nums[m]
        #     elif nums[m+1]<nums[m]:
        #         return nums[m+1]
        #     else:
        #         if nums[r]<nums[m]:
        #             l=m+1
        #         else:
        #             r=m-1
        # return l

        #Better Solution

        n = len(nums)
        l,r = 0, n-1

        while l<r:
            mid = (l+r)//2
            if nums[r]<nums[mid]:
                l=mid+1
            else:
                r=mid
        return nums[l]