class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0 #pointer to track the last unique element
        n = len(nums)
        for i in range(1,n):
            num = nums[i]
            if num != nums[idx]:
                idx+=1
                nums[idx]=num
        return idx+1