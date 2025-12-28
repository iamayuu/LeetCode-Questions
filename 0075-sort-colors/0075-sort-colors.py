class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        total_red = 0
        total_white = 0
        total_blue = 0
        for n in nums:
            if n==0:
                total_red+=1
            elif n==1:
                total_white+=1
            elif n==2:
                total_blue+=1    
        
        nums[:]=[0]*total_red+[1]*total_white+[2]*total_blue
            
        