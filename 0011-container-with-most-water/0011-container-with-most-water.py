class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Using 2 pointers
        n = len(height)
        left = 0
        right = n-1
        max_water = 0
        max_len = max(height)

        while left<right:
            area = (right-left)*min(height[left],height[right])
            max_water=max(max_water,area)
            #special condition to save time
            if max_water > max_len*(right-left):
                return max_water
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        
        return max_water