class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if len(nums)<4:
            return False
        
        first, second, third = False,False,False
        i=0
        n = len(nums)
        while i <n-1:
            if nums[i+1]>nums[i]:
                first = True
            else:
                break
            i=i+1
        while i<n-1:
            if nums[i+1]<nums[i]:
                second = True
            else:
                break
            i+=1
        while i<n-1:
            if nums[i+1]>nums[i]:
                third = True
            else:
                break
            i+=1
        return True if (first and second and third and i==n-1) else False
