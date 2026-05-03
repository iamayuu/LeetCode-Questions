class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[2]>=nums[0]+nums[1]:
            return "none"
        
        my_set = set(nums)
        n = len(my_set)
        if n==1:
            return "equilateral"
        elif n==2:
            return "isosceles"
        elif n==3:
            return "scalene"