class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        #Solution 1 (Brute Force)
        # n = len(nums)
        # for  i in range(2**n):
        #     s = bin(i)[2:].zfill(n)
        #     if s not in nums:
        #         return s

        #Solution 2 (Optimal)
        n = len(nums)
        ans = ""
        for i in range(n):
            if nums[i][i]=="1":
                ans+="0"
            else:
                ans+="1"
        return ans