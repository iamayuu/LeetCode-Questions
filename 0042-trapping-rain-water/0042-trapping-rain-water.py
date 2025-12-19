class Solution:
    def trap(self, height: List[int]) -> int:
        #Solution 1 - Array pre processing
        len_height = len(height)
        if len_height<3:
            return 0
        left_max = [0]*len_height
        right_max = [0]*len_height

        left_max[0]=height[0]
        right_max[len_height-1]=height[len_height-1]

        for i in range(len_height-1):
            left_max[i]=max(left_max[i-1],height[i])

        for i in range(len_height-2,0,-1):
            right_max[i]=max(right_max[i+1],height[i])

        result = 0
        for i in range(1,len_height-1):
            water_at_i = min(left_max[i],right_max[i])-height[i]
            water_at_i = max(0, water_at_i) #if somehow -ve water comes up
            result = result+water_at_i

        return result
