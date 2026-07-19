class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique, iterator = 0, 0
        
        for iterator in range(1,len(nums)):
            if nums[unique]!=nums[iterator]:
                unique+=1
                nums[unique]=nums[iterator]

        return unique+1