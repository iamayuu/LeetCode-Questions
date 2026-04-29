class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        m = max(height)
        ans = 0
        while l<r:
            area =  (r-l) * min(height[l],height[r])
            ans = max(ans, area)
            if ans>=m*(r-l):
                break 
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        
        return ans