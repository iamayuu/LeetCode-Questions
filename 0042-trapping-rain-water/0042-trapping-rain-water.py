class Solution:
    def trap(self, height: List[int]) -> int:
        #Solution 1 - Array pre processing
        # len_height = len(height)
        # if len_height<3:
        #     return 0
        # left_max = [0]*len_height
        # right_max = [0]*len_height

        # for i in range(len_height):
        #     if i==0:
        #         left_max[i]=height[i]
        #         right_max[len_height-1-i]=height[len_height-1-i]
        #     else:
        #         if left_max[i-1]<height[i]:
        #             left_max[i]=height[i]
        #         else:
        #             left_max[i]=left_max[i-1]
        #         if right_max[len_height-1-i+1]<height[len_height-1-i]:
        #             right_max[len_height-1-i]=height[len_height-1-i]
        #         else:
        #             right_max[len_height-1-i]=right_max[len_height-1-i+1]

        # result = 0
        # for i in range(1,len_height-1):
        #     water_at_i = min(left_max[i],right_max[i])-height[i]
        #     water_at_i = max(0, water_at_i) #if somehow -ve water comes up
        #     result = result+water_at_i

        # return result

        #Solution 2 - 2 Pointer Approach
        if len(height)<3:
            return 0
        left = 0
        right = len(height)-1
        left_max = 0
        right_max = 0
        result = 0
        while left<right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max<=right_max:
                result += left_max-height[left]
                left+=1
            else:
                result += right_max-height[right]
                right-=1
        return result

