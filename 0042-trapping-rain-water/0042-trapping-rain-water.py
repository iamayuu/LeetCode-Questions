class Solution:
    def trap(self, height: List[int]) -> int:
        #Solution 1 Arrap Preporcessing
        # n = len(height)
        # maxLeft = [0]*n
        # maxRight = [0]*n
        # maxL = 0
        # maxR = 0
        # for i in range(n):
        #     j = n-1-i #for tracking the right side
        #     maxLeft[i]=maxL
        #     maxL = max(maxL,height[i])
        #     maxRight[j]=maxR
        #     maxR = max(maxR, height[j])
        
        # print(maxLeft)
        # print(maxRight)
        # totalWater = 0
        # for i in range(1,n-1):
        #     water = max(0, min(maxLeft[i],maxRight[i])-height[i])
        #     totalWater += water
        
        # return totalWater

        #Solution2 2 Pointers
        n = len(height)
        l, r = 0, n-1
        leftMax = 0
        rightMax = 0
        totalWater = 0
        while l<r:
            leftMax = max(leftMax, height[l])
            rightMax = max(rightMax, height[r])
            if leftMax<rightMax:
                totalWater += max(0, leftMax-height[l])
                l+=1
            else:
                totalWater +=  max(0, rightMax-height[r])
                r-=1
            
        return totalWater