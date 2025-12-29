class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        while start!=end:
            mid = int((start+end)/2)
            if nums[mid]>nums[mid+1]:
                end=mid
            elif nums[mid]<nums[mid+1]:
                start=mid+1
            
        return end
