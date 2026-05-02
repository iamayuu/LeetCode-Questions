class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Solution 1 JUST SORT
        # nums.sort()

        #Solutuiom 2
        n = len(nums)
        r, b = 0, n-1
        i=0
        while i<=b:
            if nums[i]==0:
                nums[i], nums[r] = nums[r], nums[i]
                r+=1
                i+=1
            elif nums[i]==2:
                nums[i], nums[b] = nums[b], nums[i]
                b-=1
            else:
                i+=1
        