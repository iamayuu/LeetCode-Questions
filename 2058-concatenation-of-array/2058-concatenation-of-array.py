class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #Solution 1 (using loop and proper approach)
        # ans= [1]*(2*len(nums))
        # for i in range(len(nums)):
        #     ans[i],ans[i+len(nums)]=nums[i],nums[i]
        # return ans
         
        #Solution 2 (using direct formula)
        return nums+nums