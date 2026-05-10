class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        nums.sort()
        
        for i in range(1,len(nums),3):
            if nums[i]!=nums[i-1]:
                return nums[i-1]
        return nums[-1]