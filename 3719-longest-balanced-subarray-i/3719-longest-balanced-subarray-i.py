class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        #Solution1 (Brute Force)
        n = len(nums)
        ans = 0
        for i in range(n):
            odd = set()
            even = set()
            if nums[i]%2==0:
                even.add(nums[i])
            else:
                odd.add(nums[i])
            
            for j in range(i,n):
                if nums[j]%2==0:
                    even.add(nums[j])
                else:
                    odd.add(nums[j]) 
                
                if len(even)==len(odd):
                    ans=max(ans,(j-i+1))
        return ans