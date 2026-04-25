class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer = 0
        for i,num in enumerate(nums):
            if num!=0:
                nums[pointer], nums[i] = nums[i], nums[pointer]
                pointer+=1
