class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        m = 0
        n = len(nums)
        for i in range(1,n):
            if abs(nums[m])<abs(nums[i]):
                break
            m+=1
        
        l = m
        r = m+1
        ans = []
        while l>=0 or r<n:
            if r>=n or abs(nums[l])<abs(nums[r]):
                ans.append(nums[l]*nums[l])
                l-=1
            else:
                ans.append(nums[r]*nums[r])
                r+=1
        return ans