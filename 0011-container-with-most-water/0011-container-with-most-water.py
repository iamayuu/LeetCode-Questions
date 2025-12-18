class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_water = 0
        while left<right:
            water_stored = (right-left)*min(height[left],height[right])
            if water_stored>max_water:
                max_water=water_stored
            if height[left]<=height[right] :
                left+=1
            else:
                right-=1

            if max_water > (right-left)*max(height):
                break
        return max_water