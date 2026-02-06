class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        #Solution1
        nums.sort()
        n = len(nums)
        i,j = 0, 0
        max_len = float("-inf") #Maximum length of balanced subarray
        while j<n:
            if nums[j]<= nums[i]*k:
                crr_len = (j-i+1)
                max_len =  max(max_len, crr_len)
                j+=1
            else:
                i+=1
        ans = n-max_len #Total - biggest valid subarray will be our and as it has minimum removals
        return ans
            